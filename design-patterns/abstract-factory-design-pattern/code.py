from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class Factory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass


class WindowsButton(Button):
    def render(self):
        print("Rendering windows button")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering windows checkbox")


class UbuntuButton(Button):
    def render(self):
        print("Rendering Ubuntu button")


class UbuntuCheckbox(Checkbox):
    def render(self):
        print("Rendering ubuntu checkbox")


class WindowsFactory(Factory):
    def createButton(self):
        return WindowsButton()

    def createCheckbox(self):
        return WindowsCheckbox()


class UbuntuFactory(Factory):
    def createButton(self):
        return UbuntuButton()

    def createCheckbox(self):
        return UbuntuCheckbox()


class Industry:
    factoryMap = {
        "windows": WindowsFactory,
        "ubuntu": UbuntuFactory,
    }

    @staticmethod
    def returnOs(osType: str) -> Factory:
        return Industry.factoryMap.get(osType)()

def renderOs(factory: Factory):
    button = factory.createButton()
    checkbox = factory.createCheckbox()

    button.render()
    checkbox.render()

osType = "windows"
os = Industry.returnOs(osType)
renderOs(os)
