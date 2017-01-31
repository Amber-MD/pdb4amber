from .leapify import Leapify

class AmberBuilder(Leapify):
    ''' Require many programs in AmberTools (pytraj, tleap, nab, ...)

    Inheritance: AmberPDBFixer --> Leapify --> AmberBuilder
    '''

    def build_protein(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_protein
        self.parm = build_protein(*args, **kwargs)
        return self

    def build_bdna(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_bdna
        self.parm = build_bdna(*args, **kwargs)
        return self

    def build_adna(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_adna
        self.parm = build_bdna(*args, **kwargs)
        return self

    def build_arna(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_arna
        self.parm = build_bdna(*args, **kwargs)
        return self

    def solvate(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import solvate
        self.parm = solvate(self.parm, *args, **kwargs)
        return self
