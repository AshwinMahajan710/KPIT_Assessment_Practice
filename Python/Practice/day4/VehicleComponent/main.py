from BrakeSensor import BrakeSensor
from custom_exceptions import BrakeFailureException, EngineOverheatException
from EngineSensor import EngineSensor
from VehicleComponent import VehicleComponent
from typing import Dict, List, Any
from operations import filter_faulty_components, generate_health_report, sort_components_by_efficiency

def main():
    
    # custom inputs
    # t1, t2, ..... , t5 = input("")
    id_, code, reading, rpm, temperature = input("Enter atrs for engine senosor(id, code, reading, rpm ,temperature): ").split(" ")
    # atr2 = input("Enter atrs for engine senosor(id, code, reading, rpm ,temperature): ").split(" ")
    # atr3 = input("Enter atrs for engine senosor(id, code, reading, rpm ,temperature): ").split(" ")
    # atr4 = input("Enter atrs for engine senosor(id, code, reading, rpm ,temperature): ").split(" ")
    # atr5 = input("Enter atrs for engine senosor(id, code, reading, rpm ,temperature): ").split(" ")

    engine7 = EngineSensor(id_, code, int(reading), int(rpm), int(temperature))

    # Object Creation
    # o Create 3 EngineSensor objects and 2 BrakeSensor objects.
    engine1: VehicleComponent = EngineSensor("101","OK",12345,1200,129)
    engine2: VehicleComponent = EngineSensor("102","Not okay",123,3200,29)
    engine3: VehicleComponent = EngineSensor("103","OK",145,5200,130)
    brake1: VehicleComponent = BrakeSensor("104","OK",145,23,12)
    brake2: VehicleComponent = BrakeSensor("105","OK",14,53,52)

    # o Store all objects in a list called components.
    components: List[VehicleComponent] = [engine1,engine2,engine3,brake1,brake2,engine7]

    # print all object details
    print("\nAll object details: ")
    for comp in components:
        print(comp)

    # print faulty components
    print("\nFiltering faulty components: ")
    print(filter_faulty_components(components))

    # Generating healh report
    print("\nGenerating health report: ")
    print(generate_health_report(components)) 

if __name__=="__main__":
    main()