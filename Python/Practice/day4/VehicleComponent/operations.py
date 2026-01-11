from BrakeSensor import BrakeSensor
from custom_exceptions import BrakeFailureException, EngineOverheatException
from EngineSensor import EngineSensor
# from VehicleComponent import VehicleComponent
from VehicleComponent import *
from typing import Dict, List, Any, Optional
from functools import reduce


# 1. filter_faulty_components(components)
# o Return components where status != "OK".
# o Use list comprehension and isinstance() to group by type.
def filter_faulty_components(components: List[VehicleComponent]) -> List[VehicleComponent]:
    return list(filter(lambda x: x.status.upper()!='OK', components))
 
# 2. sort_components_by_efficiency(components)
# o Sort components by computed efficiency using their compute_efficiency() method.
# o Use lambda with sorted().
def sort_components_by_efficiency(components: List[VehicleComponent]) -> List[VehicleComponent]:
    return sorted(components, key= lambda x: x.compute_efficiency(), reverse=False)

# 3. generate_health_report(components)
# Output a dictionary: 
# {
#   "total_components": int,
#   "engine_alerts": List[str],
#   "brake_alerts": List[str],
#   "average_efficiency": float
# }
# Use dictionary comprehension and map().
def generate_health_report(components: List[VehicleComponent]) -> Dict[str,Any]:
    output_dict: Dict[str,Any] = {}
    output_dict["total_components"] = len(components)
    output_dict["engine_alerts"] = list(map(lambda x: x.status_message(),list(filter(lambda x: isinstance(x,EngineSensor), components))))
    output_dict["brake_alerts"] = list(map(lambda x: x.status_message(),list(filter(lambda x: isinstance(x,BrakeSensor), components))))
    output_dict["average_efficieny"] = reduce(lambda acc,x: acc + x.compute_efficiency(),components,0) 
    return output_dict