from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict

from pydantic import BaseModel, Field

class CategoryEnum(str, Enum):
    """
    Enum for Pass Culture category types.
    """
    
    ATELIER_PRATIQUE_ART = "ATELIER_PRATIQUE_ART"
    CINE_PLEIN_AIR = "CINE_PLEIN_AIR"
    CONCERT = "CONCERT"
    CONCOURS = "CONCOURS"
    CONFERENCE = "CONFERENCE"
    EVENEMENT_CINE = "EVENEMENT_CINE"
    EVENEMENT_JEU = "EVENEMENT_JEU"
    EVENEMENT_MUSIQUE = "EVENEMENT_MUSIQUE"
    EVENEMENT_PATRIMOINE = "EVENEMENT_PATRIMOINE"
    FESTIVAL_ART_VISUEL = "FESTIVAL_ART_VISUEL"
    FESTIVAL_CINE = "FESTIVAL_CINE"
    FESTIVAL_LIVRE = "FESTIVAL_LIVRE"
    FESTIVAL_MUSIQUE = "FESTIVAL_MUSIQUE"
    FESTIVAL_SPECTACLE = "FESTIVAL_SPECTACLE"
    LIVESTREAM_EVENEMENT = "LIVESTREAM_EVENEMENT"
    LIVESTREAM_MUSIQUE = "LIVESTREAM_MUSIQUE"
    LIVESTREAM_PRATIQUE_ARTISTIQUE = "LIVESTREAM_PRATIQUE_ARTISTIQUE"
    RENCONTRE = "RENCONTRE"
    RENCONTRE_EN_LIGNE = "RENCONTRE_EN_LIGNE"
    RENCONTRE_JEU = "RENCONTRE_JEU"
    SALON = "SALON"
    SEANCE_CINE = "SEANCE_CINE"
    SEANCE_ESSAI_PRATIQUE_ART = "SEANCE_ESSAI_PRATIQUE_ART"
    SPECTACLE_REPRESENTATION = "SPECTACLE_REPRESENTATION"
    VISITE = "VISITE"
    VISITE_GUIDEE = "VISITE_GUIDEE"


class CategoryRelatedFields(BaseModel):
    """
    Model representing category related fields.
    """
    category : CategoryEnum = Field(..., description="Category of the event offer")
    speaker : str = Field(..., description="Speaker or artist associated with the event offer")