"""
Contains data types modelling .csv files in ./data/

The constructors for these classes must have arguments listed in the same order as the columns in the .csv files.
"""

from __future__ import annotations
from enum import Enum, auto
import time
from typing import Union

class Boss:
    """
    World bosses in bosses.csv
    """
    def __init__(self, search_str, boss_name, image_key):
        self.search_str = search_str
        self.boss_name = boss_name
        self.image_key = image_key
    
    def __eq__(self, other: Boss) -> bool:
        if not isinstance(other, Boss):
            return False
        return (
            self.search_str == other.search_str and
            self.boss_name == other.boss_name and
            self.image_key == other.image_key
        )


class Character:
    """
    Playable characters in characters.csv
    """
    def __init__(self, search_str, image_key, character_display_name):
        self.search_str = search_str
        self.image_key = image_key
        self.character_display_name = character_display_name
    
    def __eq__(self, other: Character) -> bool:
        if not isinstance(other, Character):
            return False
        
        return (
            self.search_str == other.search_str and
            self.image_key == other.image_key and
            self.character_display_name == other.character_display_name
        )


class DomainType(Enum):
    FORGERY = 0
    BLESSING = 1
    MASTERY = 2
    TROUNCE = 3
    LIMITED_EVENT = 4 # limited time event
    ONE_TIME = 5
    """
    One time domains include story quest domains.
    """
    
    def from_str(domain_type_str: str) -> DomainType:
        """
        NOTE: The domain type values in domains.csv must match the strings here.
        """
        match domain_type_str.lower():
            case 'forgery':
                return DomainType.FORGERY
            case 'blessing':
                return DomainType.BLESSING
            case 'mastery':
                return DomainType.MASTERY
            case 'trounce':
                return DomainType.TROUNCE
            case 'limited':
                return DomainType.LIMITED_EVENT
            case 'one-time':
                return DomainType.ONE_TIME
    
    def __str__(self) -> str:
        match self.name:
            case 'FORGERY':
                return 'Domain of Forgery'
            case 'BLESSING':
                return 'Domain of Blessing'
            case 'MASTERY':
                return 'Domain of Mastery'
            case 'TROUNCE':
                return 'Trounce Domain'
            case 'LIMITED_EVENT':
                return 'Limited Time Event Domain'
            case 'ONE_TIME':
                return 'Domain'


class Domain:
    """
    From domains.csv.
    
    THe domain type values must match string values in `DomainType.from_str`
    """
    def __init__(self, search_str, domain_name, domain_type, image_key):
        self.search_str = search_str
        self.domain_name = domain_name
        self.domain_type = DomainType.from_str(domain_type)
        self.image_key = image_key
    
    def __eq__(self, other: Domain) -> bool:
        if not isinstance(other, Domain):
            return False
        
        return (
            self.search_str == other.search_str and
            self.domain_name == other.domain_name and
            self.domain_type == other.domain_type and
            self.image_key == other.image_key
        )


class Location:
    def __init__(self, search_str, location_name, subarea, country, image_key):
        self.search_str = search_str
        self.location_name = location_name
        self.subarea = subarea
        self.country = country
        self.image_key = image_key
    
    def __eq__(self, other: Location) -> bool:
        if not isinstance(other, Location):
            return False
        
        return (
            self.search_str == other.search_str and
            self.location_name == other.location_name and
            self.subarea == other.subarea and
            self.country == other.country and
            self.image_key == other.image_key
        )


class ActivityType(Enum):
    LOADING = auto()
    """
    activity_data: `False` until active character is found, then `True`.
    If `False`, display game loading message.
    If `True`, display 'Somewhere in Teyvat'.
    """
    PAUSED = auto()
    """
    Idle activity.
    activity_data: previous non-idle `Activity` object.
    """
    PARTY_SETUP = auto()
    """
    Idle activity.
    activity_data: previous non-idle `Activity` object.
    """
    DOMAIN = auto()
    """
    activity data: `Domain` object
    """
    LOCATION = auto()
    """
    activity_data: `Location` object
    """
    COMMISSION = auto()
    """
    activity_data: `None`
    """
    WORLD_BOSS = auto()
    """
    activity_data: 'Boss' object
    """


class Activity:
    def __init__(self, activity_type: ActivityType, activity_data: Union[Activity, Boss, Character, Domain, Location, None, bool]):
        self.activity_type = activity_type
        """
        Contents of `activity_data` depends on `activity_type`.
        
        See documentation for entries in `ActivityType` for what `activity_data` should contain.
        """

        self.activity_data = activity_data
        self.start_time = time.time()
    
    def is_idle(self) -> bool:
        """
        Idle activities are activity states where no active character can be found.
        """
        return self.activity_type in [ActivityType.PAUSED, ActivityType.PARTY_SETUP]

    def to_update_params_dict(self) -> dict:
        """
        Creates a dictionary with parameters for `Presence.update`.
        
        Small image and timestamp not included and should be added later.
        """
        match self.activity_type:
            case ActivityType.LOADING:
                return {
                    'state': 'Loading' if not self.activity_data else 'Somewhere in Teyvat',
                    'large_image': 'icon_paimon',
                }
            case ActivityType.PAUSED:
                return {
                    'state': 'Game paused',
                    'large_image': 'icon_paimon',
                }
            case ActivityType.PARTY_SETUP:
                return {
                    'state': 'Party Setup',
                    'large_image': 'icon_party_setup',
                }
            case ActivityType.DOMAIN:
                return {
                    'details': self.activity_data.domain_name,
                    'state': f'Clearing a domain',
                    'large_image': self.activity_data.image_key,
                    'large_text': str(self.activity_data.domain_type),
                }
            case ActivityType.LOCATION:
                if self.activity_data.subarea == '':
                    state = self.activity_data.country
                elif self.activity_data.country == '':
                    state = self.activity_data.subarea
                else:
                    state = f'{self.activity_data.subarea}, {self.activity_data.country}'
                return {
                    'details': f'Exploring {self.activity_data.location_name}',
                    'state': state,
                    'large_image': self.activity_data.image_key,
                }
            case ActivityType.COMMISSION:
                return {
                    'state': 'Doing commissions',
                    'large_image': 'icon_commission',
                }
            case ActivityType.WORLD_BOSS:
                return {
                    'state': f'Fighting a boss',
                    'details': self.activity_data.boss_name,
                    'large_image': self.activity_data.image_key,
                    'large_text': self.activity_data.boss_name,
                }

    def __eq__(self, other: Activity) -> bool:
        if not isinstance(other, Activity):
            return False
        return self.activity_type == other.activity_type and self.activity_data == other.activity_data