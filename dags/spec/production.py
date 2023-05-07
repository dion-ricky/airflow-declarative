from datetime import datetime


class billofmaterials:
    billofmaterialsid: int
    productassemblyid: int
    componentid: int
    startdate: datetime
    enddate: datetime
    unitmeasurecode: str
    bomlevel: int
    perassemblyqty: int
    modifieddate: datetime