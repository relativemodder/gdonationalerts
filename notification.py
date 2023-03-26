from dataclasses import dataclass


@dataclass
class Notification:
    title: str
    contents: str

    def as_gd_format(self):
        return "~".join([
            self.title, 
            self.contents
            ])
    
