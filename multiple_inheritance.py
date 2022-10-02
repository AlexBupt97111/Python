class AMD:
    def __init__ (self):
        print("Constructor AMD")
        super().__init__()
        
class Intel:
    def __init__(self):
        print("Constructor Intel")
        super().__init__()
        
class NVidia:
    def __init__(self):
        print("Constructor NVidia")
        super().__init__()
        
class GeForce:
    def __init__(self):
        print("Constructor GeForce")
        super().__init__()

class CPU(AMD, Intel):
    print("Constructor CPU")
    def __init__(self):
        super().__init__()

    def setProcessor(self, processor: str, cpuCores: int = None, cpuFrequency: float = None):#setter
        if cpuCores is None and cpuFrequency is None:
            self._processor = processor
        else:
            self._processor = processor
            self._cpuCores = cpuCores
            self._cpuFrequency = cpuFrequency#use setter
        
class GPU (NVidia, GeForce):
    print("Constructor GPU")
    def __init__(self):
        super().__init__()# if use super().

    def setVideoCard(self, videoCard: str, gpuCores: int = None, gpuMemory: int = None):
        if gpuCores is None and gpuMemory is None:
            self._videoCard = videoCard
        else:
            self._videoCard = videoCard
            self._gpuCores = gpuCores
            self._gpuMemory = gpuMemory
class Memory:
    def __init__(self):
        print("Constructor Memory")
        super().__init__()

def setMemory(self, memoryVolume: int, memoryFrequency: int):#setter
        self._memoryVolume = memoryVolume
        self._memoryFrequency = memoryFrequency


class Motherboard(CPU,GPU,Memory):
    def __init__(self,processor: str, cpuCores: int, cpuFrequency: float, \
                 videoCard: str, gpuCores: int, gpuMemory: int, \
                 memoryVolume: int, memoryFrequency: int):
        self._processor = processor
        self._cpuCores = cpuCores
        self._cpuFrequency = cpuFrequency
        self._videoCard = videoCard
        self._gpuCores = gpuCores
        self._gpuMemory = gpuMemory
        self._memoryVolume = memoryVolume
        self._memoryFrequency = memoryFrequency
        super().__init__()

    def showInfo(self):
        print(f"Processor: {self._processor}\n\
CPU: cores - {self._cpuCores}, frequency - {self._cpuFrequency}\n\
Video Card: {self._videoCard}\n\
GPU: cores - {self._gpuCores}, memory - {self._gpuMemory}\n\
RAM: volume - {self._memoryVolume}, frequency - {self._memoryFrequency}")

m = Motherboard("AMD Ryzen 7 2700x", 8, 3.7, "GeForce 1080 Ti", 3584, 8, 8, 3200)

m.showInfo()
