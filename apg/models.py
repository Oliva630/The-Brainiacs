from django.db import models
import re

# Create your models here.
class ApgChromosome(models.Model):
    chromosome_name = models.CharField(db_column='Chromosome_Name', max_length=25)  # Field name made lowercase.
    start = models.CharField(db_column='Start', max_length=10)  # Field name made lowercase.
    end = models.CharField(db_column='End', max_length=10)  # Field name made lowercase.
    orientation = models.CharField(db_column='Orientation', max_length=1)  # Field name made lowercase.
    contig_name = models.OneToOneField('ApgContig', models.DO_NOTHING, db_column='Contig_Name_id')  # Field name made lowercase.

    class Meta:
        db_table = 'apg_chromosome'


class ApgContig(models.Model):
    contig_name = models.CharField(db_column='Contig_Name', primary_key=True, max_length=25)  # Field name made lowercase.
    contig_place_condition = models.CharField(db_column='Contig_Place_Condition', max_length=3)  # Field name made lowercase.
    contig_length = models.IntegerField(db_column='Contig_Length')  # Field name made lowercase.
    contig_sequence = models.TextField(db_column='Contig_Sequence')  # Field name made lowercase.
    num_individuals = models.IntegerField(db_column='Num_Individuals')  # Field name made lowercase.s

    class Meta:
        db_table = 'apg_contig'


class ApgGene(models.Model):
    gene_type = models.CharField(db_column='Gene_Type', max_length=7)  # Field name made lowercase.
    gene_name = models.CharField(db_column='Gene_Name', max_length=20)  # Field name made lowercase.
    contig_name = models.ForeignKey(ApgContig, models.DO_NOTHING, db_column='Contig_Name_id')  # Field name made lowercase.
    entrez_id = models.CharField(db_column='Entrez_Id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hgnc_id = models.CharField(db_column='HGNC_Id', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ncbi_url = models.CharField(db_column='NCBI_Url', max_length=50, blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'apg_gene'


class ApgScaffold(models.Model):
    align_scaffold_name = models.CharField(db_column='Align_Scaffold_Name', max_length=20)  # Field name made lowercase.
    align_start = models.CharField(db_column='Align_Start', max_length=10)  # Field name made lowercase.
    align_end = models.CharField(db_column='Align_End', max_length=10)  # Field name made lowercase.
    align_coverage = models.FloatField(db_column='Align_Coverage')  # Field name made lowercase.
    align_identity = models.FloatField(db_column='Align_Identity')  # Field name made lowercase.
    contig_name = models.ForeignKey(ApgContig, models.DO_NOTHING, db_column='Contig_Name_id')  # Field name made lowercase.

    class Meta:
        db_table = 'apg_scaffold'





