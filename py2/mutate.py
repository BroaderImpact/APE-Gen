# pymol -qc mutate.py pdb selection new_residue
# example: pymol -qc mutate.py 0.pdb C/1/ ALA 0_mutated.pdb

# run for all the confs in the ensemble
# append all to one using mdconvert

from pymol import cmd
import sys

pdb, selection, mutant, output_name = sys.argv[-4:]
print "file:", pdb
print "selection:", selection
print "mutating to:", mutant
print "output name:", output_name

cmd.load(pdb, "file")

cmd.wizard("mutagenesis")
cmd.refresh_wizard()
cmd.get_wizard().do_select(selection)
cmd.get_wizard().set_mode(mutant)
cmd.get_wizard().apply()
cmd.set_wizard()

cmd.save(output_name, "file")
