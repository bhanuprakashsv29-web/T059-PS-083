from dataclasses import dataclass
from datetime import date
from typing import Optional
@dataclass
class BOMLine:
    parent_item:str; component_item:str; quantity:float; effective_from:date; effective_to:Optional[date]
