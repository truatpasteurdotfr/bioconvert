from bioconvert.fastq2fasta_qual import FASTQ2FASTA_QUAL
from bioconvert.fasta_qual2fastq import FASTA_QUAL2FASTQ
from bioconvert import bioconvert_data
from easydev import TempFile, md5


# TODO: Add test of the unwrap_fasta method
def test_conv():
    infile = bioconvert_data("ERR.fastq")
    md1 = md5(infile)

    with TempFile(suffix=".fasta") as fout1, TempFile(suffix=".qual") as fout2:
        c = FASTQ2FASTA_QUAL(infile, (fout1.name, fout2.name))
        c()

        with TempFile(suffix=".fastq") as fout3:
            c = FASTA_QUAL2FASTQ((fout1.name, fout2.name), fout3.name)
            c()
            md2  = md5(fout3.name)
    assert md1 == md2



