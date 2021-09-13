class Developer():
    def __init__(self) -> None:
        self._seniority = 'Junior'
        self.skills = ''

    def display(self):
        print("x {seniority} developer skills {skills}".format(
            seniority=self._seniority, skills=self.skills
        ))


class NodeJs(Developer):
    def __init__(self) -> None:
        super().__init__()
        self._seniority = 'Senior'
        self.skills = 'NodeJS'


if __name__ == '__main__':
    c = NodeJs()
    c.display()