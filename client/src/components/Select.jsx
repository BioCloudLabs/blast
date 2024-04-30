export const Select = ({ value, setValue }) => {
    return (
        <>
            <div className="p-0.5 rounded-lg bg-gradient-to-br from-green-400 to-blue-600 mb-12">
                <select className="text-center bg-slate-200 rounded-lg w-96 p-2.5 focus:outline-none" value={value} onChange={(event) => setValue(event.target.value)}>
                    <option value="16S_ribosomal_RNA">16S ribosomal RNA (Bacteria and Archaea type strains)</option>
                    <option value="18S_fungal_sequences">18S ribosomal RNA sequences (SSU) from Fungi type and reference material</option>
                    <option value="28S_fungal_sequences">28S ribosomal RNA sequences (LSU) from Fungi type and reference material</option>
                    <option value="Betacoronavirus">Betacoronavirus</option>
                    <option value="GCF_000001405.38_top_level">Homo sapiens GRCh38.p12 [GCF_000001405.38] chromosomes plus unplaced and unlocalized scaffolds</option>
                    <option value="GCF_000001635.26_top_level">Mus musculus GRCm38.p6 [GCF_000001635.26] chromosomes plus unplaced and unlocalized scaffolds</option>
                    <option value="ITS_RefSeq_Fungi">Internal transcribed spacer region (ITS) from Fungi type and reference material</option>
                    <option value="ITS_eukaryote_sequences">ITS eukaryote BLAST</option>
                    <option value="LSU_eukaryote_rRNA">Large subunit ribosomal nucleic acid for Eukaryotes</option>
                    <option value="LSU_prokaryote_rRNA">Large subunit ribosomal nucleic acid for Prokaryotes</option>
                    <option value="SSU_eukaryote_rRNA">Small subunit ribosomal nucleic acid for Eukaryotes</option>
                    <option value="env_nt">environmental samples</option>
                    <option value="nt">Nucleotide collection (nt)</option>
                    <option value="patnt">Nucleotide sequences derived from the Patent division of GenBank</option>
                    <option value="pdbnt">PDB nucleotide database</option>
                    <option value="ref_euk_rep_genomes">RefSeq Eukaryotic Representative Genome Database</option>
                    <option value="ref_prok_rep_genomes">Refseq prokaryote representative genomes (contains refseq assembly)</option>
                    <option value="ref_viroids_rep_genomes">Refseq viroids representative genomes</option>
                    <option value="ref_viruses_rep_genomes">Refseq viruses representative genomes</option>
                    <option value="refseq_rna">NCBI Transcript Reference Sequences</option>
                    <option value="refseq_select_rna">RefSeq Select RNA sequences</option>
                    <option value="tsa_nt">Transcriptome Shotgun Assembly (TSA) sequences</option>
                    <option value="env_nr">Proteins from WGS metagenomic projects</option>
                    <option value="landmark">Landmark database for SmartBLAST</option>
                    <option value="nr">All non-redundant GenBank CDS translations+PDB+SwissProt+PIR+PRF excluding environmental samples from WGS projects</option>
                    <option value="pdbaa">PDB protein database</option>
                    <option value="pataa">Protein sequences derived from the Patent division of GenBank</option>
                    <option value="refseq_protein">NCBI Protein Reference Sequences</option>
                    <option value="refseq_select_prot">RefSeq Select proteins</option>
                    <option value="swissprot">Non-redundant UniProtKB/SwissProt sequences</option>
                    <option value="tsa_nr">Transcriptome Shotgun Assembly (TSA) sequences</option>
                    <option value="cdd">Conserved Domain Database (CDD) is a collection of well-annotated multiple sequence alignment models reprepresented as position-specific score matrices</option>
                </select>
            </div>
            <div className="text-center">
                {!value && 'No Search Set Choosed'}
            </div>
        </>
    )
}