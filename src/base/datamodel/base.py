# Auto generated from base.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-28T01:25:53
# Schema: base
#
# id: https://w3id.org/lmodel/base
# description: Entity and association taxonomy and datamodel for named thing abstractions.
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime

metamodel_version = "1.7.0"
version = "0.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CDAO = CurieNamespace('CDAO', 'http://purl.obolibrary.org/obo/CDAO_')
CIO = CurieNamespace('CIO', 'http://purl.obolibrary.org/obo/CIO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://purl.org/coar/resource_type/')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTD = CurieNamespace('CTD', 'http://ctdbase.org/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
CVE = CurieNamespace('CVE', 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=')
ECO = CurieNamespace('ECO', 'https://evidenceontology.org/term/')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
EXO = CurieNamespace('EXO', 'http://purl.obolibrary.org/obo/ExO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
GR = CurieNamespace('GR', 'http://purl.org/goodrelations/v1#')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
IDO = CurieNamespace('IDO', 'http://purl.obolibrary.org/obo/IDO_')
INO = CurieNamespace('INO', 'http://purl.obolibrary.org/obo/INO_')
LCSH = CurieNamespace('LCSH', 'http://id.loc.gov/authorities/subjects/')
LCSH_PUB = CurieNamespace('LCSH_PUB', 'http://id.loc.gov/vocabulary/mgovtpubtype/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MI = CurieNamespace('MI', 'http://purl.obolibrary.org/obo/MI_')
MMO = CurieNamespace('MMO', 'http://purl.obolibrary.org/obo/MMO_')
NBO = CurieNamespace('NBO', 'http://purl.obolibrary.org/obo/NBO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OBO = CurieNamespace('OBO', 'http://purl.obolibrary.org/obo/')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/pato#')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN.html#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
ASTROVOCAB = CurieNamespace('astrovocab', 'https://www.asc-csa.gc.ca/eng/resources/vocabulary/view.asp?id=')
BASE = CurieNamespace('base', 'https://w3id.org/lmodel/base/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DBO = CurieNamespace('dbo', 'https://dbpedia.org/ontology/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DCTYPES = CurieNamespace('dctypes', 'http://purl.org/dc/dcmitype/')
DOI = CurieNamespace('doi', 'https://doi.org/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
FREEDICT = CurieNamespace('freedict', 'https://www.thefreedictionary.com/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
ISBN = CurieNamespace('isbn', 'https://www.isbn-international.org/identifier/')
ISNI = CurieNamespace('isni', 'https://isni.org/isni/')
ISSN = CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
METASAT = CurieNamespace('metasat', 'https://schema.space/metasat/')
OPENVOCAB = CurieNamespace('openvocab', 'https://vocab.org/open/#')
OS = CurieNamespace('os', 'https://github.com/cmungall/owlstar/blob/master/owlstar.ttl')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'https://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'https://www.w3.org/TR/vocab-ssn/#')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
SUMO_WN = CurieNamespace('sumo-wn', 'https://w3id.org/sumo/wn/')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/UBERON_')
UCO_CORE = CurieNamespace('uco-core', 'https://unifiedcyberontology.org/ontology/uco/core#')
UCO_OBSERVABLE = CurieNamespace('uco-observable', 'https://unifiedcyberontology.org/ontology/uco/observable#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BASE


# Types
class FormulaValue(str):
    """ A formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "formula value"
    type_model_uri = BASE.FormulaValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the base model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the base class, for example base:Service. For an RDF representation, the value should be a URI such as https://w3id.org/lmodel/base/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = BASE.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = BASE.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = BASE.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the base related_to hierarchy. For example, base:related_to, base:causes, base:treats """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = BASE.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = BASE.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = BASE.SymbolType


class FrequencyValue(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency value"
    type_model_uri = BASE.FrequencyValue


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = BASE.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = BASE.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = BASE.Unit


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = BASE.TimeType


class ComputationalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "computational sequence"
    type_model_uri = BASE.ComputationalSequence


# Class references
class NamedThingId(extended_str):
    pass


class PersonId(NamedThingId):
    pass


class OntologyClassId(extended_str):
    pass


class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class AttributeId(NamedThingId):
    pass


class ControlRoleId(AttributeId):
    pass


class BiologicalSexId(AttributeId):
    pass


class SeverityValueId(AttributeId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class SystemTaxonId(NamedThingId):
    pass


class EventId(NamedThingId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class StudyResultId(InformationContentEntityId):
    pass


class StudyId(InformationContentEntityId):
    pass


class StudyVariableId(InformationContentEntityId):
    pass


class CommonDataElementId(InformationContentEntityId):
    pass


class TextMiningResultId(StudyResultId):
    pass


class ChiSquaredAnalysisResultId(StudyResultId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DatasetDistributionId(InformationContentEntityId):
    pass


class DatasetVersionId(InformationContentEntityId):
    pass


class DatasetSummaryId(InformationContentEntityId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class InformationResourceId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BookId(PublicationId):
    pass


class BookChapterId(PublicationId):
    pass


class SerialId(PublicationId):
    pass


class ArticleId(PublicationId):
    pass


class PhysicalEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class ProcedureId(NamedThingId):
    pass


class PhenomenonId(NamedThingId):
    pass


class DeviceId(NamedThingId):
    pass


class MaterialSampleId(PhysicalEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class ComputationalEntityId(NamedThingId):
    pass


class ControlEntityId(NamedThingId):
    pass


class OperationalEntityId(ControlEntityId):
    pass


class ControlMixtureId(ControlEntityId):
    pass


class RedundancyEntityId(OperationalEntityId):
    pass


class OperationalMixtureId(ControlMixtureId):
    pass


class ComplexOperationalMixtureId(ControlMixtureId):
    pass


class ComputationalProcessOrActivityId(ComputationalEntityId):
    pass


class OperationalActivityId(ComputationalProcessOrActivityId):
    pass


class ComputationalProcessId(ComputationalProcessOrActivityId):
    pass


class PathwayId(ComputationalProcessId):
    pass


class BehaviorId(ComputationalProcessId):
    pass


class ProcessedMaterialId(ControlMixtureId):
    pass


class AdministrativeOperationId(OperationalMixtureId):
    pass


class SystemAttributeId(AttributeId):
    pass


class ObservableQualityId(SystemAttributeId):
    pass


class InheritanceId(ComputationalEntityId):
    pass


class SystemEntityId(ComputationalEntityId):
    pass


class ComponentSystemId(SystemEntityId):
    pass


class LifecycleStageId(SystemEntityId):
    pass


class IndividualSystemId(SystemEntityId):
    pass


class PopulationOfIndividualSystemsId(SystemEntityId):
    pass


class StudyPopulationId(PopulationOfIndividualSystemsId):
    pass


class FaultOrObservableFeatureId(ComputationalEntityId):
    pass


class FaultId(FaultOrObservableFeatureId):
    pass


class ObservableFeatureId(FaultOrObservableFeatureId):
    pass


class BehavioralFeatureId(ObservableFeatureId):
    pass


class DeploymentEntityId(SystemEntityId):
    pass


class ComponentId(DeploymentEntityId):
    pass


class ComponentTypeId(SystemEntityId):
    pass


class ClassId(ComputationalEntityId):
    pass


class AssemblyComplexId(ComputationalEntityId):
    pass


class WorkloadId(ComputationalEntityId):
    pass


class ReplicaId(RedundancyEntityId):
    pass


class SystemOperationId(ComputationalEntityId):
    pass


class SystemOperationDomainId(ComputationalEntityId):
    pass


class HomogeneityId(AttributeId):
    pass


class ServiceTypeId(ComputationalEntityId):
    pass


class EmpiricalAttributeId(AttributeId):
    pass


class EmpiricalMeasurementId(EmpiricalAttributeId):
    pass


class EmpiricalModifierId(EmpiricalAttributeId):
    pass


class EmpiricalCourseId(EmpiricalAttributeId):
    pass


class OnsetId(EmpiricalCourseId):
    pass


class EmpiricalEntityId(NamedThingId):
    pass


class EmpiricalInterventionId(EmpiricalEntityId):
    pass


class EmpiricalFindingId(ObservableFeatureId):
    pass


class OfflineMaintenanceId(EmpiricalInterventionId):
    pass


class SocioeconomicAttributeId(AttributeId):
    pass


class CaseId(IndividualSystemId):
    pass


class CohortId(StudyPopulationId):
    pass


class ExposureEventId(OntologyClassId):
    pass


class WorkloadBackgroundExposureId(AttributeId):
    pass


class FaultyProcessId(ComputationalProcessId):
    pass


class FaultyProcessExposureId(AttributeId):
    pass


class FaultyDeploymentStructureId(SystemEntityId):
    pass


class FaultyDeploymentExposureId(AttributeId):
    pass


class FaultOrObservableFeatureExposureId(FaultOrObservableFeatureId):
    pass


class ControlExposureId(AttributeId):
    pass


class AdministrativeOperationExposureId(ControlExposureId):
    pass


class RestorationId(NamedThingId):
    pass


class EnvironmentalExposureId(AttributeId):
    pass


class GeographicExposureId(EnvironmentalExposureId):
    pass


class BehavioralExposureId(AttributeId):
    pass


class SocioeconomicExposureId(AttributeId):
    pass


class AssociationId(EntityId):
    pass


class ControlEntityAssessesNamedThingAssociationId(AssociationId):
    pass


class ContributorAssociationId(AssociationId):
    pass


class ServiceTypeToServiceTypePartAssociationId(AssociationId):
    pass


class ServiceTypeToClassAssociationId(AssociationId):
    pass


class ClassToClassAssociationId(AssociationId):
    pass


class ControlToControlAssociationId(AssociationId):
    pass


class ReactionToParticipantAssociationId(ControlToControlAssociationId):
    pass


class ReactionToCatalystAssociationId(ReactionToParticipantAssociationId):
    pass


class ControlToFaultOrObservableFeatureAssociationId(AssociationId):
    pass


class ClassToPathwayAssociationId(AssociationId):
    pass


class OperationalActivityToPathwayAssociationId(AssociationId):
    pass


class ControlToPathwayAssociationId(AssociationId):
    pass


class AdministrativeOperationToClassAssociationId(AssociationId):
    pass


class FaultToExposureEventAssociationId(AssociationId):
    pass


class ExposureEventToOutcomeAssociationId(AssociationId):
    pass


class InformationContentEntityToNamedThingAssociationId(AssociationId):
    pass


class FaultOrObservableFeatureToLocationAssociationId(AssociationId):
    pass


class ServiceTypeToObservableFeatureAssociationId(AssociationId):
    pass


class ExposureEventToObservableFeatureAssociationId(AssociationId):
    pass


class FaultToObservableFeatureAssociationId(AssociationId):
    pass


class CaseToObservableFeatureAssociationId(AssociationId):
    pass


class BehaviorToBehavioralFeatureAssociationId(AssociationId):
    pass


class ClassToObservableFeatureAssociationId(AssociationId):
    pass


class ClassToFaultAssociationId(AssociationId):
    pass


class ControllableClassToFaultAssociationId(ClassToFaultAssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class ServiceTypeToFaultAssociationId(AssociationId):
    pass


class SystemToSystemAssociationId(AssociationId):
    pass


class TaxonToTaxonAssociationId(AssociationId):
    pass


class ClassToExpressionSiteAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class AssemblyToOperationalActivityAssociationId(FunctionalAssociationId):
    pass


class AssemblyToComputationalProcessAssociationId(FunctionalAssociationId):
    pass


class AssemblyToComponentAssociationId(FunctionalAssociationId):
    pass


class EntityToFaultAssociationId(AssociationId):
    pass


class EntityToObservableFeatureAssociationId(AssociationId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = BASE.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    Represents a Person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Person
    class_class_curie: ClassVar[str] = "base:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = BASE.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A holder for Person objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.PersonCollection
    class_class_curie: ClassVar[str] = "base:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = BASE.PersonCollection

    entries: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(YAMLRoot):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a base compatible KG can be
    considered both instances of base classes, and OWL classes in their own right. In general you should not need to
    use this class directly. Instead, use the appropriate base class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.OntologyClass
    class_class_curie: ClassVar[str] = "base:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = BASE.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Baselink Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Annotation
    class_class_curie: ClassVar[str] = "base:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = BASE.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.QuantityValue
    class_class_curie: ClassVar[str] = "base:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = BASE.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


class RelationshipQuantifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.RelationshipQuantifier
    class_class_curie: ClassVar[str] = "base:RelationshipQuantifier"
    class_name: ClassVar[str] = "relationship quantifier"
    class_model_uri: ClassVar[URIRef] = BASE.RelationshipQuantifier


class SensitivityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SensitivityQuantifier
    class_class_curie: ClassVar[str] = "base:SensitivityQuantifier"
    class_name: ClassVar[str] = "sensitivity quantifier"
    class_model_uri: ClassVar[URIRef] = BASE.SensitivityQuantifier


class SpecificityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SpecificityQuantifier
    class_class_curie: ClassVar[str] = "base:SpecificityQuantifier"
    class_name: ClassVar[str] = "specificity quantifier"
    class_model_uri: ClassVar[URIRef] = BASE.SpecificityQuantifier


@dataclass
class FrequencyQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FrequencyQuantifier
    class_class_curie: ClassVar[str] = "base:FrequencyQuantifier"
    class_name: ClassVar[str] = "frequency quantifier"
    class_model_uri: ClassVar[URIRef] = BASE.FrequencyQuantifier

    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


class ControlOrAdministrativeOperationOrRestoration(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlOrAdministrativeOperationOrRestoration
    class_class_curie: ClassVar[str] = "base:ControlOrAdministrativeOperationOrRestoration"
    class_name: ClassVar[str] = "control or administrative operation or restoration"
    class_model_uri: ClassVar[URIRef] = BASE.ControlOrAdministrativeOperationOrRestoration


@dataclass
class Entity(YAMLRoot):
    """
    Root Baselink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Entity
    class_class_curie: ClassVar[str] = "base:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = BASE.Entity

    id: Union[str, EntityId] = None
    iri: Optional[Union[str, IriType]] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    has_attribute: Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, AttributeId) else AttributeId(v) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = BASE.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    provided_by: Optional[Union[str, List[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if not isinstance(self.provided_by, list):
            self.provided_by = [self.provided_by] if self.provided_by is not None else []
        self.provided_by = [v if isinstance(v, str) else str(v) for v in self.provided_by]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class Attribute(NamedThing):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Attribute
    class_class_curie: ClassVar[str] = "base:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = BASE.Attribute

    id: Union[str, AttributeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)

        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value] if self.has_quantitative_value is not None else []
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.has_quantitative_value]

        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        super().__post_init__(**kwargs)


@dataclass
class ControlRole(Attribute):
    """
    A role played by the entity or part thereof within a control context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlRole
    class_class_curie: ClassVar[str] = "base:ControlRole"
    class_name: ClassVar[str] = "control role"
    class_model_uri: ClassVar[URIRef] = BASE.ControlRole

    id: Union[str, ControlRoleId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlRoleId):
            self.id = ControlRoleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.BiologicalSex
    class_class_curie: ClassVar[str] = "base:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = BASE.BiologicalSex

    id: Union[str, BiologicalSexId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a observable feature or fault
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SeverityValue
    class_class_curie: ClassVar[str] = "base:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = BASE.SeverityValue

    id: Union[str, SeverityValueId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.RelationshipType
    class_class_curie: ClassVar[str] = "base:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = BASE.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.TaxonomicRank
    class_class_curie: ClassVar[str] = "base:TaxonomicRank"
    class_name: ClassVar[str] = "taxonomic rank"
    class_model_uri: ClassVar[URIRef] = BASE.TaxonomicRank

    id: Union[str, TaxonomicRankId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonomicRankId):
            self.id = TaxonomicRankId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemTaxon(NamedThing):
    """
    A classification of a set of systems. Example instances: Can also be used to represent subsystems.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SystemTaxon
    class_class_curie: ClassVar[str] = "base:SystemTaxon"
    class_name: ClassVar[str] = "system taxon"
    class_model_uri: ClassVar[URIRef] = BASE.SystemTaxon

    id: Union[str, SystemTaxonId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemTaxonId):
            self.id = SystemTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        super().__post_init__(**kwargs)


@dataclass
class Event(NamedThing):
    """
    Something that happens at a given place and time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Event
    class_class_curie: ClassVar[str] = "base:Event"
    class_name: ClassVar[str] = "event"
    class_model_uri: ClassVar[URIRef] = BASE.Event

    id: Union[str, EventId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AdministrativeEntity
    class_class_curie: ClassVar[str] = "base:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = BASE.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Agent
    class_class_curie: ClassVar[str] = "base:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = BASE.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.InformationContentEntity
    class_class_curie: ClassVar[str] = "base:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = BASE.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class StudyResult(InformationContentEntity):
    """
    A collection of data items from a study that are about a particular study subject or experimental unit (the
    'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of
    this data as evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.StudyResult
    class_class_curie: ClassVar[str] = "base:StudyResult"
    class_name: ClassVar[str] = "study result"
    class_model_uri: ClassVar[URIRef] = BASE.StudyResult

    id: Union[str, StudyResultId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Study(InformationContentEntity):
    """
    a detailed investigation and/or analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Study
    class_class_curie: ClassVar[str] = "base:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = BASE.Study

    id: Union[str, StudyId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class StudyVariable(InformationContentEntity):
    """
    a variable that is used as a measure in the investigation of a study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.StudyVariable
    class_class_curie: ClassVar[str] = "base:StudyVariable"
    class_name: ClassVar[str] = "study variable"
    class_model_uri: ClassVar[URIRef] = BASE.StudyVariable

    id: Union[str, StudyVariableId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyVariableId):
            self.id = StudyVariableId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CommonDataElement(InformationContentEntity):
    """
    A Common Data Element (CDE) is a standardized, precisely defined question, paired with a set of allowable
    responses, used systematically across different sites, studies, or clinical trials to ensure consistent data
    collection. Multiple CDEs (from one or more Collections) can be curated into Forms. (https://cde.nlm.nih.gov/home)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.CommonDataElement
    class_class_curie: ClassVar[str] = "base:CommonDataElement"
    class_name: ClassVar[str] = "common data element"
    class_model_uri: ClassVar[URIRef] = BASE.CommonDataElement

    id: Union[str, CommonDataElementId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommonDataElementId):
            self.id = CommonDataElementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TextMiningResult(StudyResult):
    """
    A result of text mining.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.TextMiningResult
    class_class_curie: ClassVar[str] = "base:TextMiningResult"
    class_name: ClassVar[str] = "text mining result"
    class_model_uri: ClassVar[URIRef] = BASE.TextMiningResult

    id: Union[str, TextMiningResultId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextMiningResultId):
            self.id = TextMiningResultId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChiSquaredAnalysisResult(StudyResult):
    """
    A result of a chi squared analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ChiSquaredAnalysisResult
    class_class_curie: ClassVar[str] = "base:ChiSquaredAnalysisResult"
    class_name: ClassVar[str] = "chi squared analysis result"
    class_model_uri: ClassVar[URIRef] = BASE.ChiSquaredAnalysisResult

    id: Union[str, ChiSquaredAnalysisResultId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChiSquaredAnalysisResultId):
            self.id = ChiSquaredAnalysisResultId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Dataset
    class_class_curie: ClassVar[str] = "base:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = BASE.Dataset

    id: Union[str, DatasetId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.DatasetDistribution
    class_class_curie: ClassVar[str] = "base:DatasetDistribution"
    class_name: ClassVar[str] = "dataset distribution"
    class_model_uri: ClassVar[URIRef] = BASE.DatasetDistribution

    id: Union[str, DatasetDistributionId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    distribution_download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetDistributionId):
            self.id = DatasetDistributionId(self.id)

        if self.distribution_download_url is not None and not isinstance(self.distribution_download_url, str):
            self.distribution_download_url = str(self.distribution_download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetVersion(InformationContentEntity):
    """
    an item that holds version level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.DatasetVersion
    class_class_curie: ClassVar[str] = "base:DatasetVersion"
    class_name: ClassVar[str] = "dataset version"
    class_model_uri: ClassVar[URIRef] = BASE.DatasetVersion

    id: Union[str, DatasetVersionId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_dataset: Optional[Union[str, DatasetId]] = None
    ingest_date: Optional[str] = None
    has_distribution: Optional[Union[str, DatasetDistributionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetVersionId):
            self.id = DatasetVersionId(self.id)

        if self.has_dataset is not None and not isinstance(self.has_dataset, DatasetId):
            self.has_dataset = DatasetId(self.has_dataset)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.has_distribution is not None and not isinstance(self.has_distribution, DatasetDistributionId):
            self.has_distribution = DatasetDistributionId(self.has_distribution)

        super().__post_init__(**kwargs)


@dataclass
class DatasetSummary(InformationContentEntity):
    """
    an item that holds summary level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.DatasetSummary
    class_class_curie: ClassVar[str] = "base:DatasetSummary"
    class_name: ClassVar[str] = "dataset summary"
    class_model_uri: ClassVar[URIRef] = BASE.DatasetSummary

    id: Union[str, DatasetSummaryId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    source_web_page: Optional[str] = None
    source_logo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetSummaryId):
            self.id = DatasetSummaryId(self.id)

        if self.source_web_page is not None and not isinstance(self.source_web_page, str):
            self.source_web_page = str(self.source_web_page)

        if self.source_logo is not None and not isinstance(self.source_logo, str):
            self.source_logo = str(self.source_logo)

        super().__post_init__(**kwargs)


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ConfidenceLevel
    class_class_curie: ClassVar[str] = "base:ConfidenceLevel"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = BASE.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EvidenceType
    class_class_curie: ClassVar[str] = "base:EvidenceType"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = BASE.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to
    consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single
    Information Resource by this definition may span many different datasets or databases, and include many access
    endpoints and user interfaces. Information Resources include project-specific resources such as a Translator
    Knowledge Provider, and community knowledgebases.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.InformationResource
    class_class_curie: ClassVar[str] = "base:InformationResource"
    class_name: ClassVar[str] = "information resource"
    class_model_uri: ClassVar[URIRef] = BASE.InformationResource

    id: Union[str, InformationResourceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationResourceId):
            self.id = InformationResourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed materials, either directly or in one of the Publication Baselink category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Publication
    class_class_curie: ClassVar[str] = "base:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = BASE.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    lcsh_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.lcsh_terms, list):
            self.lcsh_terms = [self.lcsh_terms] if self.lcsh_terms is not None else []
        self.lcsh_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.lcsh_terms]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Book(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Book
    class_class_curie: ClassVar[str] = "base:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = BASE.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class BookChapter(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.BookChapter
    class_class_curie: ClassVar[str] = "base:BookChapter"
    class_name: ClassVar[str] = "book chapter"
    class_model_uri: ClassVar[URIRef] = BASE.BookChapter

    id: Union[str, BookChapterId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    volume: Optional[str] = None
    chapter: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookChapterId):
            self.id = BookChapterId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        super().__post_init__(**kwargs)


@dataclass
class Serial(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Serial
    class_class_curie: ClassVar[str] = "base:Serial"
    class_name: ClassVar[str] = "serial"
    class_model_uri: ClassVar[URIRef] = BASE.Serial

    id: Union[str, SerialId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SerialId):
            self.id = SerialId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


@dataclass
class Article(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Article
    class_class_curie: ClassVar[str] = "base:Article"
    class_name: ClassVar[str] = "article"
    class_model_uri: ClassVar[URIRef] = BASE.Article

    id: Union[str, ArticleId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArticleId):
            self.id = ArticleId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


class TangibleEssenceOrOccurrent(YAMLRoot):
    """
    Either a physical or processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.TangibleEssenceOrOccurrent
    class_class_curie: ClassVar[str] = "base:TangibleEssenceOrOccurrent"
    class_name: ClassVar[str] = "tangible essence or occurrent"
    class_model_uri: ClassVar[URIRef] = BASE.TangibleEssenceOrOccurrent


class TangibleEssence(TangibleEssenceOrOccurrent):
    """
    Semantic mixin concept. Pertains to entities that have tangible properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.TangibleEssence
    class_class_curie: ClassVar[str] = "base:TangibleEssence"
    class_name: ClassVar[str] = "tangible essence"
    class_model_uri: ClassVar[URIRef] = BASE.TangibleEssence


@dataclass
class PhysicalEntity(NamedThing):
    """
    An entity that has material reality (a.k.a. tangible essence).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.PhysicalEntity
    class_class_curie: ClassVar[str] = "base:PhysicalEntity"
    class_name: ClassVar[str] = "physical entity"
    class_model_uri: ClassVar[URIRef] = BASE.PhysicalEntity

    id: Union[str, PhysicalEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalEntityId):
            self.id = PhysicalEntityId(self.id)

        super().__post_init__(**kwargs)


class Occurrent(TangibleEssenceOrOccurrent):
    """
    A processual entity that has temporal parts and happens, unfolds or develops through time. Occurrents have phases.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Occurrent
    class_class_curie: ClassVar[str] = "base:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = BASE.Occurrent


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "base:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = BASE.ActivityAndBehavior


@dataclass
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Activity
    class_class_curie: ClassVar[str] = "base:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = BASE.Activity

    id: Union[str, ActivityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Procedure(NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Procedure
    class_class_curie: ClassVar[str] = "base:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = BASE.Procedure

    id: Union[str, ProcedureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Phenomenon
    class_class_curie: ClassVar[str] = "base:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = BASE.Phenomenon

    id: Union[str, PhenomenonId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Device
    class_class_curie: ClassVar[str] = "base:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = BASE.Device

    id: Union[str, DeviceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)


class SubjectOfInvestigation(YAMLRoot):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SubjectOfInvestigation
    class_class_curie: ClassVar[str] = "base:SubjectOfInvestigation"
    class_name: ClassVar[str] = "subject of investigation"
    class_model_uri: ClassVar[URIRef] = BASE.SubjectOfInvestigation


@dataclass
class MaterialSample(PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.MaterialSample
    class_class_curie: ClassVar[str] = "base:MaterialSample"
    class_name: ClassVar[str] = "material sample"
    class_model_uri: ClassVar[URIRef] = BASE.MaterialSample

    id: Union[str, MaterialSampleId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.PlanetaryEntity
    class_class_curie: ClassVar[str] = "base:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = BASE.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "base:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = BASE.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "base:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = BASE.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.GeographicLocation
    class_class_curie: ClassVar[str] = "base:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = BASE.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.GeographicLocationAtTime
    class_class_curie: ClassVar[str] = "base:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = BASE.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems;
    named things, their groups and other operational entities; parts and processes
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.ThingWithTaxon
    class_class_curie: ClassVar[str] = "base:ThingWithTaxon"
    class_name: ClassVar[str] = "thing with taxon"
    class_model_uri: ClassVar[URIRef] = BASE.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.ComputationalEntity
    class_class_curie: ClassVar[str] = "base:ComputationalEntity"
    class_name: ClassVar[str] = "computational entity"
    class_model_uri: ClassVar[URIRef] = BASE.ComputationalEntity

    id: Union[str, ComputationalEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class WorkloadEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.WorkloadEntity
    class_class_curie: ClassVar[str] = "base:WorkloadEntity"
    class_name: ClassVar[str] = "workload entity"
    class_model_uri: ClassVar[URIRef] = BASE.WorkloadEntity

    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class ControlEntity(NamedThing):
    """
    A control entity is a entity that pertains to control or orchestration
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlEntity
    class_class_curie: ClassVar[str] = "base:ControlEntity"
    class_name: ClassVar[str] = "control entity"
    class_model_uri: ClassVar[URIRef] = BASE.ControlEntity

    id: Union[str, ControlEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    trade_name: Optional[Union[str, ControlEntityId]] = None
    available_from: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    is_toxic: Optional[Union[bool, Bool]] = None
    has_control_role: Optional[Union[Union[str, ControlRoleId], List[Union[str, ControlRoleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlEntityId):
            self.id = ControlEntityId(self.id)

        if self.trade_name is not None and not isinstance(self.trade_name, ControlEntityId):
            self.trade_name = ControlEntityId(self.trade_name)

        if not isinstance(self.available_from, list):
            self.available_from = [self.available_from] if self.available_from is not None else []
        self.available_from = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.available_from]

        if self.is_toxic is not None and not isinstance(self.is_toxic, Bool):
            self.is_toxic = Bool(self.is_toxic)

        if not isinstance(self.has_control_role, list):
            self.has_control_role = [self.has_control_role] if self.has_control_role is not None else []
        self.has_control_role = [v if isinstance(v, ControlRoleId) else ControlRoleId(v) for v in self.has_control_role]

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntity(ControlEntity):
    """
    A operational entity is a control entity composed of individual or bonded elements
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.OperationalEntity
    class_class_curie: ClassVar[str] = "base:OperationalEntity"
    class_name: ClassVar[str] = "operational entity"
    class_model_uri: ClassVar[URIRef] = BASE.OperationalEntity

    id: Union[str, OperationalEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    is_controller: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalEntityId):
            self.id = OperationalEntityId(self.id)

        if self.is_controller is not None and not isinstance(self.is_controller, Bool):
            self.is_controller = Bool(self.is_controller)

        super().__post_init__(**kwargs)


@dataclass
class ControlMixture(ControlEntity):
    """
    A control mixture is a control entity composed of two or more operational entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlMixture
    class_class_curie: ClassVar[str] = "base:ControlMixture"
    class_name: ClassVar[str] = "control mixture"
    class_model_uri: ClassVar[URIRef] = BASE.ControlMixture

    id: Union[str, ControlMixtureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    is_supplement: Optional[Union[str, ControlMixtureId]] = None
    highest_regulator_approval_status: Optional[str] = None
    administrative_operation_regulatory_status_world_wide: Optional[str] = None
    routes_of_delivery: Optional[Union[Union[str, "DeliveryEnum"], List[Union[str, "DeliveryEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlMixtureId):
            self.id = ControlMixtureId(self.id)

        if self.is_supplement is not None and not isinstance(self.is_supplement, ControlMixtureId):
            self.is_supplement = ControlMixtureId(self.is_supplement)

        if self.highest_regulator_approval_status is not None and not isinstance(self.highest_regulator_approval_status, str):
            self.highest_regulator_approval_status = str(self.highest_regulator_approval_status)

        if self.administrative_operation_regulatory_status_world_wide is not None and not isinstance(self.administrative_operation_regulatory_status_world_wide, str):
            self.administrative_operation_regulatory_status_world_wide = str(self.administrative_operation_regulatory_status_world_wide)

        if not isinstance(self.routes_of_delivery, list):
            self.routes_of_delivery = [self.routes_of_delivery] if self.routes_of_delivery is not None else []
        self.routes_of_delivery = [v if isinstance(v, DeliveryEnum) else DeliveryEnum(v) for v in self.routes_of_delivery]

        super().__post_init__(**kwargs)


@dataclass
class RedundancyEntity(OperationalEntity):
    """
    A redundancy entity is a operational entity
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.RedundancyEntity
    class_class_curie: ClassVar[str] = "base:RedundancyEntity"
    class_name: ClassVar[str] = "redundancy entity"
    class_model_uri: ClassVar[URIRef] = BASE.RedundancyEntity

    id: Union[str, RedundancyEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RedundancyEntityId):
            self.id = RedundancyEntityId(self.id)

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class OperationalMixture(ControlMixture):
    """
    A operational mixture is a control mixture composed of two or more operational entities with known concentration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.OperationalMixture
    class_class_curie: ClassVar[str] = "base:OperationalMixture"
    class_name: ClassVar[str] = "operational mixture"
    class_model_uri: ClassVar[URIRef] = BASE.OperationalMixture

    id: Union[str, OperationalMixtureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalMixtureId):
            self.id = OperationalMixtureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComplexOperationalMixture(ControlMixture):
    """
    A complex operational mixture is a control mixture composed of two or more operational entities with unknown
    concentration
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ComplexOperationalMixture
    class_class_curie: ClassVar[str] = "base:ComplexOperationalMixture"
    class_name: ClassVar[str] = "complex operational mixture"
    class_model_uri: ClassVar[URIRef] = BASE.ComplexOperationalMixture

    id: Union[str, ComplexOperationalMixtureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplexOperationalMixtureId):
            self.id = ComplexOperationalMixtureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcessOrActivity(ComputationalEntity):
    """
    Either an individual operational activity, or a collection of causally connected operational activities
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BASE.ComputationalProcessOrActivity
    class_class_curie: ClassVar[str] = "base:ComputationalProcessOrActivity"
    class_name: ClassVar[str] = "computational process or activity"
    class_model_uri: ClassVar[URIRef] = BASE.ComputationalProcessOrActivity

    id: Union[str, ComputationalProcessOrActivityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_input: Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, SystemEntityId], List[Union[str, SystemEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputationalProcessOrActivityId):
            self.id = ComputationalProcessOrActivityId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, ComputationalProcessOrActivityId) else ComputationalProcessOrActivityId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ComputationalProcessOrActivityId) else ComputationalProcessOrActivityId(v) for v in self.has_output]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, SystemEntityId) else SystemEntityId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class OperationalActivity(ComputationalProcessOrActivity):
    """
    An execution of a operational function carried out by a subclasses or assembly complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BASE.OperationalActivity
    class_class_curie: ClassVar[str] = "base:OperationalActivity"
    class_name: ClassVar[str] = "operational activity"
    class_model_uri: ClassVar[URIRef] = BASE.OperationalActivity

    id: Union[str, OperationalActivityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_input: Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]] = empty_list()
    has_output: Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "AssemblyMixin"], List[Union[dict, "AssemblyMixin"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalActivityId):
            self.id = OperationalActivityId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, OperationalEntityId) else OperationalEntityId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, OperationalEntityId) else OperationalEntityId(v) for v in self.has_output]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, AssemblyMixin) else AssemblyMixin(**as_dict(v)) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcess(ComputationalProcessOrActivity):
    """
    One or more causally connected executions of operational functions
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BASE.ComputationalProcess
    class_class_curie: ClassVar[str] = "base:ComputationalProcess"
    class_name: ClassVar[str] = "computational process"
    class_model_uri: ClassVar[URIRef] = BASE.ComputationalProcess

    id: Union[str, ComputationalProcessId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputationalProcessId):
            self.id = ComputationalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BASE.Pathway
    class_class_curie: ClassVar[str] = "base:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = BASE.Pathway

    id: Union[str, PathwayId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Behavior(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BASE.Behavior
    class_class_curie: ClassVar[str] = "base:Behavior"
    class_name: ClassVar[str] = "behavior"
    class_model_uri: ClassVar[URIRef] = BASE.Behavior

    id: Union[str, BehaviorId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProcessedMaterial(ControlMixture):
    """
    A control entity (often a mixture) processed for some use. Is an entity created or changed during processing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ProcessedMaterial
    class_class_curie: ClassVar[str] = "base:ProcessedMaterial"
    class_name: ClassVar[str] = "processed material"
    class_model_uri: ClassVar[URIRef] = BASE.ProcessedMaterial

    id: Union[str, ProcessedMaterialId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessedMaterialId):
            self.id = ProcessedMaterialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperation(OperationalMixture):
    """
    A event intended for use in the operational administration, mitigation, repair, or prevention of fault
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AdministrativeOperation
    class_class_curie: ClassVar[str] = "base:AdministrativeOperation"
    class_name: ClassVar[str] = "administrative operation"
    class_model_uri: ClassVar[URIRef] = BASE.AdministrativeOperation

    id: Union[str, AdministrativeOperationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationId):
            self.id = AdministrativeOperationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemAttribute(Attribute):
    """
    describes a characteristic of an system entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SystemAttribute
    class_class_curie: ClassVar[str] = "base:SystemAttribute"
    class_name: ClassVar[str] = "system attribute"
    class_model_uri: ClassVar[URIRef] = BASE.SystemAttribute

    id: Union[str, SystemAttributeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemAttributeId):
            self.id = SystemAttributeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObservableQuality(SystemAttribute):
    """
    A property of a observable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ObservableQuality
    class_class_curie: ClassVar[str] = "base:ObservableQuality"
    class_name: ClassVar[str] = "observable quality"
    class_model_uri: ClassVar[URIRef] = BASE.ObservableQuality

    id: Union[str, ObservableQualityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableQualityId):
            self.id = ObservableQualityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Inheritance(ComputationalEntity):
    """
    The pattern or 'mode' in which a particular acquired trait or disorder is passed from one generation to the next
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Inheritance
    class_class_curie: ClassVar[str] = "base:Inheritance"
    class_name: ClassVar[str] = "inheritance"
    class_model_uri: ClassVar[URIRef] = BASE.Inheritance

    id: Union[str, InheritanceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InheritanceId):
            self.id = InheritanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemEntity(ComputationalEntity):
    """
    A named entity that is either a part of a system, a whole system, population or clade of systems, excluding
    control entities
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.SystemEntity
    class_class_curie: ClassVar[str] = "base:SystemEntity"
    class_name: ClassVar[str] = "system entity"
    class_model_uri: ClassVar[URIRef] = BASE.SystemEntity

    id: Union[str, SystemEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute: Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, AttributeId) else AttributeId(v) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class ComponentSystem(SystemEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.ComponentSystem
    class_class_curie: ClassVar[str] = "base:ComponentSystem"
    class_name: ClassVar[str] = "component system"
    class_model_uri: ClassVar[URIRef] = BASE.ComponentSystem

    id: Union[str, ComponentSystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentSystemId):
            self.id = ComponentSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class LifecycleStage(SystemEntity):
    """
    A stage of development or growth of a system.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.LifecycleStage
    class_class_curie: ClassVar[str] = "base:LifecycleStage"
    class_name: ClassVar[str] = "lifecycle stage"
    class_model_uri: ClassVar[URIRef] = BASE.LifecycleStage

    id: Union[str, LifecycleStageId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifecycleStageId):
            self.id = LifecycleStageId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class IndividualSystem(SystemEntity):
    """
    An instance of an system. For example, human. Computer, my pet cat.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.IndividualSystem
    class_class_curie: ClassVar[str] = "base:IndividualSystem"
    class_name: ClassVar[str] = "individual system"
    class_model_uri: ClassVar[URIRef] = BASE.IndividualSystem

    id: Union[str, IndividualSystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualSystemId):
            self.id = IndividualSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PopulationOfIndividualSystems(SystemEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, acquireds, observable features.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.PopulationOfIndividualSystems
    class_class_curie: ClassVar[str] = "base:PopulationOfIndividualSystems"
    class_name: ClassVar[str] = "population of individual systems"
    class_model_uri: ClassVar[URIRef] = BASE.PopulationOfIndividualSystems

    id: Union[str, PopulationOfIndividualSystemsId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationOfIndividualSystemsId):
            self.id = PopulationOfIndividualSystemsId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class StudyPopulation(PopulationOfIndividualSystems):
    """
    A group of individuals banded together as a group as participants in a research study.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.StudyPopulation
    class_class_curie: ClassVar[str] = "base:StudyPopulation"
    class_name: ClassVar[str] = "study population"
    class_model_uri: ClassVar[URIRef] = BASE.StudyPopulation

    id: Union[str, StudyPopulationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyPopulationId):
            self.id = StudyPopulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultOrObservableFeature(ComputationalEntity):
    """
    Either one of a fault or an individual observable feature.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeature
    class_class_curie: ClassVar[str] = "base:FaultOrObservableFeature"
    class_name: ClassVar[str] = "fault or observable feature"
    class_model_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeature

    id: Union[str, FaultOrObservableFeatureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultOrObservableFeatureId):
            self.id = FaultOrObservableFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Fault(FaultOrObservableFeature):
    """
    A disorder of structure or function, especially one that produces specific signs, observable features or symptoms
    or that affects a specific location and is not simply a direct result of injury.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Fault
    class_class_curie: ClassVar[str] = "base:Fault"
    class_name: ClassVar[str] = "fault"
    class_model_uri: ClassVar[URIRef] = BASE.Fault

    id: Union[str, FaultId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultId):
            self.id = FaultId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObservableFeature(FaultOrObservableFeature):
    """
    A combination of entity and quality that makes up a observation statement. An observable characteristic of an
    element resulting from the interaction of its observable feature with its operational and tangible environment.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.ObservableFeature
    class_class_curie: ClassVar[str] = "base:ObservableFeature"
    class_name: ClassVar[str] = "observable feature"
    class_model_uri: ClassVar[URIRef] = BASE.ObservableFeature

    id: Union[str, ObservableFeatureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableFeatureId):
            self.id = ObservableFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralFeature(ObservableFeature):
    """
    A observable feature which is behavioral in nature.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.BehavioralFeature
    class_class_curie: ClassVar[str] = "base:BehavioralFeature"
    class_name: ClassVar[str] = "behavioral feature"
    class_model_uri: ClassVar[URIRef] = BASE.BehavioralFeature

    id: Union[str, BehavioralFeatureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralFeatureId):
            self.id = BehavioralFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntity(SystemEntity):
    """
    A process location, or gross deployment part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.DeploymentEntity
    class_class_curie: ClassVar[str] = "base:DeploymentEntity"
    class_name: ClassVar[str] = "deployment entity"
    class_model_uri: ClassVar[URIRef] = BASE.DeploymentEntity

    id: Union[str, DeploymentEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeploymentEntityId):
            self.id = DeploymentEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Component(DeploymentEntity):
    """
    The component is the smallest system entity that can be deployed, isolated, and restored independently. A
    self-contained assembly of parts within a complete operating unit or module, which cannot be further subdivided
    without loss of identity or function.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Component
    class_class_curie: ClassVar[str] = "base:Component"
    class_name: ClassVar[str] = "component"
    class_model_uri: ClassVar[URIRef] = BASE.Component

    id: Union[str, ComponentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentType(SystemEntity):
    """
    A component type defines the set of components running the same software and sharing the same configuration. It's
    a single point of configuration control.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.ComponentType
    class_class_curie: ClassVar[str] = "base:ComponentType"
    class_name: ClassVar[str] = "component type"
    class_model_uri: ClassVar[URIRef] = BASE.ComponentType

    id: Union[str, ComponentTypeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentTypeId):
            self.id = ComponentTypeId(self.id)

        super().__post_init__(**kwargs)


class ControlEntityOrClassOrSubclasses(YAMLRoot):
    """
    A union of control entities and subclasses, and class or subclasses. This mixin is helpful to use when searching
    across control entities that must include classes and their subclasses as control entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlEntityOrClassOrSubclasses
    class_class_curie: ClassVar[str] = "base:ControlEntityOrClassOrSubclasses"
    class_name: ClassVar[str] = "control entity or class or subclasses"
    class_model_uri: ClassVar[URIRef] = BASE.ControlEntityOrClassOrSubclasses


class ControlEntityOrSystemOperation(YAMLRoot):
    """
    A union of control entities and subclasses, and system operation. This mixin is helpful to use when searching
    across control entities that must include system operations and their subclasses as control entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlEntityOrSystemOperation
    class_class_curie: ClassVar[str] = "base:ControlEntityOrSystemOperation"
    class_name: ClassVar[str] = "control entity or system operation"
    class_model_uri: ClassVar[URIRef] = BASE.ControlEntityOrSystemOperation


@dataclass
class AssemblyMixin(YAMLRoot):
    """
    The functional group of a single named thing locus. groups are either system operations or functional operations A
    union of class, subclass, and assembly complex. These are the basic units of function in a component. They either
    carry out individual computational activities, or they encode operations which do this.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AssemblyMixin
    class_class_curie: ClassVar[str] = "base:AssemblyMixin"
    class_name: ClassVar[str] = "assembly mixin"
    class_model_uri: ClassVar[URIRef] = BASE.AssemblyMixin

    name: Optional[Union[str, SymbolType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)

        super().__post_init__(**kwargs)


class ClassOrSubclasses(AssemblyMixin):
    """
    A union of class or subclasses. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassOrSubclasses
    class_class_curie: ClassVar[str] = "base:ClassOrSubclasses"
    class_name: ClassVar[str] = "class or subclasses"
    class_model_uri: ClassVar[URIRef] = BASE.ClassOrSubclasses


@dataclass
class Class(ComputationalEntity):
    """
    collection of items in an ontology sharing common characteristics. Classes provide an abstraction mechanism for
    grouping resources with similar characteristics.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Class
    class_class_curie: ClassVar[str] = "base:Class"
    class_name: ClassVar[str] = "class"
    class_model_uri: ClassVar[URIRef] = BASE.Class

    id: Union[str, ClassId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    symbol: Optional[str] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassId):
            self.id = ClassId(self.id)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class SubclassesMixin(ClassOrSubclasses):
    """
    The functional operational product of a single class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SubclassesMixin
    class_class_curie: ClassVar[str] = "base:SubclassesMixin"
    class_name: ClassVar[str] = "subclasses mixin"
    class_model_uri: ClassVar[URIRef] = BASE.SubclassesMixin

    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class AssemblyComplex(ComputationalEntity):
    """
    A stable assembly of two or more assemblies, i.e. system operation, redundancy entity, etc, in which at least one
    component is a system operation and the constituent parts function together
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.AssemblyComplex
    class_class_curie: ClassVar[str] = "base:AssemblyComplex"
    class_name: ClassVar[str] = "assembly complex"
    class_model_uri: ClassVar[URIRef] = BASE.AssemblyComplex

    id: Union[str, AssemblyComplexId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssemblyComplexId):
            self.id = AssemblyComplexId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Workload(ComputationalEntity):
    """
    A workload is the sum of acquired material within a named thing.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Workload
    class_class_curie: ClassVar[str] = "base:Workload"
    class_name: ClassVar[str] = "workload"
    class_model_uri: ClassVar[URIRef] = BASE.Workload

    id: Union[str, WorkloadId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkloadId):
            self.id = WorkloadId(self.id)

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class Replica(RedundancyEntity):
    """
    The unit of service workload the component is capable of providing or protecting.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Replica
    class_class_curie: ClassVar[str] = "base:Replica"
    class_name: ClassVar[str] = "replica"
    class_model_uri: ClassVar[URIRef] = BASE.Replica

    id: Union[str, ReplicaId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReplicaId):
            self.id = ReplicaId(self.id)

        super().__post_init__(**kwargs)


class NamedSequence(WorkloadEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.NamedSequence
    class_class_curie: ClassVar[str] = "base:NamedSequence"
    class_name: ClassVar[str] = "named sequence"
    class_model_uri: ClassVar[URIRef] = BASE.NamedSequence


@dataclass
class SystemOperation(ComputationalEntity):
    """
    A group that is composed of a chain of instructions and is produced by translation of service message
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.SystemOperation
    class_class_curie: ClassVar[str] = "base:SystemOperation"
    class_name: ClassVar[str] = "system operation"
    class_model_uri: ClassVar[URIRef] = BASE.SystemOperation

    id: Union[str, SystemOperationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemOperationId):
            self.id = SystemOperationId(self.id)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)


@dataclass
class SystemOperationDomain(ComputationalEntity):
    """
    The domain the system operation belongs to.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.SystemOperationDomain
    class_class_curie: ClassVar[str] = "base:SystemOperationDomain"
    class_name: ClassVar[str] = "system operation domain"
    class_model_uri: ClassVar[URIRef] = BASE.SystemOperationDomain

    id: Union[str, SystemOperationDomainId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_class_or_subclasses: Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemOperationDomainId):
            self.id = SystemOperationDomainId(self.id)

        if not isinstance(self.has_class_or_subclasses, list):
            self.has_class_or_subclasses = [self.has_class_or_subclasses] if self.has_class_or_subclasses is not None else []
        self.has_class_or_subclasses = [v if isinstance(v, ClassId) else ClassId(v) for v in self.has_class_or_subclasses]

        super().__post_init__(**kwargs)


@dataclass
class ClassGroupingMixin(YAMLRoot):
    """
    any grouping of multiple classes or subclasses
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassGroupingMixin
    class_class_curie: ClassVar[str] = "base:ClassGroupingMixin"
    class_name: ClassVar[str] = "class grouping mixin"
    class_model_uri: ClassVar[URIRef] = BASE.ClassGroupingMixin

    has_class_or_subclasses: Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_class_or_subclasses, list):
            self.has_class_or_subclasses = [self.has_class_or_subclasses] if self.has_class_or_subclasses is not None else []
        self.has_class_or_subclasses = [v if isinstance(v, ClassId) else ClassId(v) for v in self.has_class_or_subclasses]

        super().__post_init__(**kwargs)


@dataclass
class Homogeneity(Attribute):
    """
    the quality or state of being all the same or all of the same kind.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Homogeneity
    class_class_curie: ClassVar[str] = "base:Homogeneity"
    class_name: ClassVar[str] = "homogeneity"
    class_model_uri: ClassVar[URIRef] = BASE.Homogeneity

    id: Union[str, HomogeneityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HomogeneityId):
            self.id = HomogeneityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ServiceType(ComputationalEntity):
    """
    An information content entity that describes a workload by specifying the total variation in workload sequence
    and/or workload expression, relative to some established background
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.ServiceType
    class_class_curie: ClassVar[str] = "base:ServiceType"
    class_name: ClassVar[str] = "service type"
    class_model_uri: ClassVar[URIRef] = BASE.ServiceType

    id: Union[str, ServiceTypeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_homogeneity: Optional[Union[str, HomogeneityId]] = None
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceTypeId):
            self.id = ServiceTypeId(self.id)

        if self.has_homogeneity is not None and not isinstance(self.has_homogeneity, HomogeneityId):
            self.has_homogeneity = HomogeneityId(self.has_homogeneity)

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalAttribute(Attribute):
    """
    Attributes relating to a empirical manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalAttribute
    class_class_curie: ClassVar[str] = "base:EmpiricalAttribute"
    class_name: ClassVar[str] = "empirical attribute"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalAttribute

    id: Union[str, EmpiricalAttributeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalAttributeId):
            self.id = EmpiricalAttributeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalMeasurement(EmpiricalAttribute):
    """
    A empirical measurement is a special kind of attribute which results from a quality of entity observation from a
    subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalMeasurement
    class_class_curie: ClassVar[str] = "base:EmpiricalMeasurement"
    class_name: ClassVar[str] = "empirical measurement"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalMeasurement

    id: Union[str, EmpiricalMeasurementId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalMeasurementId):
            self.id = EmpiricalMeasurementId(self.id)

        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalModifier(EmpiricalAttribute):
    """
    Used to characterize and specify the observable changes with respect to severity, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalModifier
    class_class_curie: ClassVar[str] = "base:EmpiricalModifier"
    class_name: ClassVar[str] = "empirical modifier"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalModifier

    id: Union[str, EmpiricalModifierId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalModifierId):
            self.id = EmpiricalModifierId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalCourse(EmpiricalAttribute):
    """
    The course an entity typically takes from its onset, progression in time, and eventual resolution or termination
    of affected entity, without obstruction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalCourse
    class_class_curie: ClassVar[str] = "base:EmpiricalCourse"
    class_name: ClassVar[str] = "empirical course"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalCourse

    id: Union[str, EmpiricalCourseId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalCourseId):
            self.id = EmpiricalCourseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Onset(EmpiricalCourse):
    """
    The beginning or start in which manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Onset
    class_class_curie: ClassVar[str] = "base:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = BASE.Onset

    id: Union[str, OnsetId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalEntity(NamedThing):
    """
    Any entity or process that exists in the empirical domain and outside the computational realm. Failures are placed
    under computational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalEntity
    class_class_curie: ClassVar[str] = "base:EmpiricalEntity"
    class_name: ClassVar[str] = "empirical entity"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalEntity

    id: Union[str, EmpiricalEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalEntityId):
            self.id = EmpiricalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalIntervention(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalIntervention
    class_class_curie: ClassVar[str] = "base:EmpiricalIntervention"
    class_name: ClassVar[str] = "empirical intervention"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalIntervention

    id: Union[str, EmpiricalInterventionId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalInterventionId):
            self.id = EmpiricalInterventionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalFinding(ObservableFeature):
    """
    this category is currently considered broad enough to tag empirical lab measurements and other computational
    attributes taken as 'empirical traits' with some statistical score, for example, a p value in acquired
    associations.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.EmpiricalFinding
    class_class_curie: ClassVar[str] = "base:EmpiricalFinding"
    class_name: ClassVar[str] = "empirical finding"
    class_model_uri: ClassVar[URIRef] = BASE.EmpiricalFinding

    id: Union[str, EmpiricalFindingId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute: Optional[Union[Union[str, EmpiricalAttributeId], List[Union[str, EmpiricalAttributeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalFindingId):
            self.id = EmpiricalFindingId(self.id)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, EmpiricalAttributeId) else EmpiricalAttributeId(v) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenance(EmpiricalIntervention):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.OfflineMaintenance
    class_class_curie: ClassVar[str] = "base:OfflineMaintenance"
    class_name: ClassVar[str] = "offline maintenance"
    class_model_uri: ClassVar[URIRef] = BASE.OfflineMaintenance

    id: Union[str, OfflineMaintenanceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfflineMaintenanceId):
            self.id = OfflineMaintenanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SocioeconomicAttribute
    class_class_curie: ClassVar[str] = "base:SocioeconomicAttribute"
    class_name: ClassVar[str] = "socioeconomic attribute"
    class_model_uri: ClassVar[URIRef] = BASE.SocioeconomicAttribute

    id: Union[str, SocioeconomicAttributeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocioeconomicAttributeId):
            self.id = SocioeconomicAttributeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Case(IndividualSystem):
    """
    An individual instance of a particular situation; an example of something occuring
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Case
    class_class_curie: ClassVar[str] = "base:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = BASE.Case

    id: Union[str, CaseId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cohort(StudyPopulation):
    """
    A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a
    particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.Cohort
    class_class_curie: ClassVar[str] = "base:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = BASE.Cohort

    id: Union[str, CohortId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(OntologyClass):
    """
    A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more
    observable feature of that system, potentially mediated by named things
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ExposureEvent
    class_class_curie: ClassVar[str] = "base:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = BASE.ExposureEvent

    id: Union[str, ExposureEventId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class WorkloadBackgroundExposure(Attribute):
    """
    A workload background exposure is where an individual's specific workload background of named things, sequences or
    other pre-existing workload conditions constitute a kind of 'exposure' to the system, leading to or influencing an
    outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.WorkloadBackgroundExposure
    class_class_curie: ClassVar[str] = "base:WorkloadBackgroundExposure"
    class_name: ClassVar[str] = "workload background exposure"
    class_model_uri: ClassVar[URIRef] = BASE.WorkloadBackgroundExposure

    id: Union[str, WorkloadBackgroundExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None
    has_class_or_subclasses: Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]] = empty_list()
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkloadBackgroundExposureId):
            self.id = WorkloadBackgroundExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if not isinstance(self.has_class_or_subclasses, list):
            self.has_class_or_subclasses = [self.has_class_or_subclasses] if self.has_class_or_subclasses is not None else []
        self.has_class_or_subclasses = [v if isinstance(v, ClassId) else ClassId(v) for v in self.has_class_or_subclasses]

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


class FaultyEntityMixin(YAMLRoot):
    """
    A faulty (abnormal) structure or process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultyEntityMixin
    class_class_curie: ClassVar[str] = "base:FaultyEntityMixin"
    class_name: ClassVar[str] = "faulty entity mixin"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyEntityMixin


@dataclass
class FaultyProcess(ComputationalProcess):
    """
    A computational function or a process having an abnormal or deleterious effect at the process, component,
    component type, or system level.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BASE.FaultyProcess
    class_class_curie: ClassVar[str] = "base:FaultyProcess"
    class_name: ClassVar[str] = "faulty process"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyProcess

    id: Union[str, FaultyProcessId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyProcessId):
            self.id = FaultyProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyProcessExposure(Attribute):
    """
    A faulty process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome,
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultyProcessExposure
    class_class_curie: ClassVar[str] = "base:FaultyProcessExposure"
    class_name: ClassVar[str] = "faulty process exposure"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyProcessExposure

    id: Union[str, FaultyProcessExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyProcessExposureId):
            self.id = FaultyProcessExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentStructure(SystemEntity):
    """
    An deployment structure with the potential of have an abnormal or deleterious effect at the process, component,
    system, or group level.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.FaultyDeploymentStructure
    class_class_curie: ClassVar[str] = "base:FaultyDeploymentStructure"
    class_name: ClassVar[str] = "faulty deployment structure"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyDeploymentStructure

    id: Union[str, FaultyDeploymentStructureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyDeploymentStructureId):
            self.id = FaultyDeploymentStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentExposure(Attribute):
    """
    An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or
    influencing an outcome,
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultyDeploymentExposure
    class_class_curie: ClassVar[str] = "base:FaultyDeploymentExposure"
    class_name: ClassVar[str] = "faulty deployment exposure"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyDeploymentExposure

    id: Union[str, FaultyDeploymentExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyDeploymentExposureId):
            self.id = FaultyDeploymentExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultOrObservableFeatureExposure(FaultOrObservableFeature):
    """
    A fault or observable feature state, when viewed as an exposure, represents an precondition, leading to or
    influencing an outcome
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureExposure
    class_class_curie: ClassVar[str] = "base:FaultOrObservableFeatureExposure"
    class_name: ClassVar[str] = "fault or observable feature exposure"
    class_model_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureExposure

    id: Union[str, FaultOrObservableFeatureExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultOrObservableFeatureExposureId):
            self.id = FaultOrObservableFeatureExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ControlExposure(Attribute):
    """
    A control exposure is an intake of a particular control entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlExposure
    class_class_curie: ClassVar[str] = "base:ControlExposure"
    class_name: ClassVar[str] = "control exposure"
    class_model_uri: ClassVar[URIRef] = BASE.ControlExposure

    id: Union[str, ControlExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlExposureId):
            self.id = ControlExposureId(self.id)

        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value] if self.has_quantitative_value is not None else []
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.has_quantitative_value]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationExposure(ControlExposure):
    """
    An intake of a particular administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AdministrativeOperationExposure
    class_class_curie: ClassVar[str] = "base:AdministrativeOperationExposure"
    class_name: ClassVar[str] = "administrative operation exposure"
    class_model_uri: ClassVar[URIRef] = BASE.AdministrativeOperationExposure

    id: Union[str, AdministrativeOperationExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationExposureId):
            self.id = AdministrativeOperationExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class Restoration(NamedThing):
    """
    A restoration is targeted at a fault or observable feature and may involve multiple administrative operation
    'exposures', engineering devices and/or procedures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Restoration
    class_class_curie: ClassVar[str] = "base:Restoration"
    class_name: ClassVar[str] = "restoration"
    class_model_uri: ClassVar[URIRef] = BASE.Restoration

    id: Union[str, RestorationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_administrative_operation: Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]] = empty_list()
    has_device: Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestorationId):
            self.id = RestorationId(self.id)

        if not isinstance(self.has_administrative_operation, list):
            self.has_administrative_operation = [self.has_administrative_operation] if self.has_administrative_operation is not None else []
        self.has_administrative_operation = [v if isinstance(v, AdministrativeOperationId) else AdministrativeOperationId(v) for v in self.has_administrative_operation]

        if not isinstance(self.has_device, list):
            self.has_device = [self.has_device] if self.has_device is not None else []
        self.has_device = [v if isinstance(v, DeviceId) else DeviceId(v) for v in self.has_device]

        if not isinstance(self.has_procedure, list):
            self.has_procedure = [self.has_procedure] if self.has_procedure is not None else []
        self.has_procedure = [v if isinstance(v, ProcedureId) else ProcedureId(v) for v in self.has_procedure]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalExposure(Attribute):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EnvironmentalExposure
    class_class_curie: ClassVar[str] = "base:EnvironmentalExposure"
    class_name: ClassVar[str] = "environmental exposure"
    class_model_uri: ClassVar[URIRef] = BASE.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class GeographicExposure(EnvironmentalExposure):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.GeographicExposure
    class_class_curie: ClassVar[str] = "base:GeographicExposure"
    class_name: ClassVar[str] = "geographic exposure"
    class_model_uri: ClassVar[URIRef] = BASE.GeographicExposure

    id: Union[str, GeographicExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicExposureId):
            self.id = GeographicExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralExposure(Attribute):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.BehavioralExposure
    class_class_curie: ClassVar[str] = "base:BehavioralExposure"
    class_name: ClassVar[str] = "behavioral exposure"
    class_model_uri: ClassVar[URIRef] = BASE.BehavioralExposure

    id: Union[str, BehavioralExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralExposureId):
            self.id = BehavioralExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicExposure(Attribute):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g.
    poverty).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SocioeconomicExposure
    class_class_curie: ClassVar[str] = "base:SocioeconomicExposure"
    class_name: ClassVar[str] = "socioeconomic exposure"
    class_model_uri: ClassVar[URIRef] = BASE.SocioeconomicExposure

    id: Union[str, SocioeconomicExposureId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    has_attribute: Union[Union[str, SocioeconomicAttributeId], List[Union[str, SocioeconomicAttributeId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocioeconomicExposureId):
            self.id = SocioeconomicExposureId(self.id)

        if self._is_empty(self.has_attribute):
            self.MissingRequiredField("has_attribute")
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, SocioeconomicAttributeId) else SocioeconomicAttributeId(v) for v in self.has_attribute]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


class Outcome(YAMLRoot):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible computational or non-computational (e.g. empirical) outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Outcome
    class_class_curie: ClassVar[str] = "base:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = BASE.Outcome


class FaultyProcessOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the manifestation of a faulty process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultyProcessOutcome
    class_class_curie: ClassVar[str] = "base:FaultyProcessOutcome"
    class_name: ClassVar[str] = "faulty process outcome"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyProcessOutcome


class FaultyDeploymentOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal deployment structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultyDeploymentOutcome
    class_class_curie: ClassVar[str] = "base:FaultyDeploymentOutcome"
    class_name: ClassVar[str] = "faulty deployment outcome"
    class_model_uri: ClassVar[URIRef] = BASE.FaultyDeploymentOutcome


class FaultOrObservableFeatureOutcome(YAMLRoot):
    """
    logical outcomes resulting from an exposure event which is the manifestation of a fault or other characteristic
    observable feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureOutcome
    class_class_curie: ClassVar[str] = "base:FaultOrObservableFeatureOutcome"
    class_name: ClassVar[str] = "fault or observable feature outcome"
    class_model_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureOutcome


class BehavioralOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the manifestation of some behavior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.BehavioralOutcome
    class_class_curie: ClassVar[str] = "base:BehavioralOutcome"
    class_name: ClassVar[str] = "behavioral outcome"
    class_model_uri: ClassVar[URIRef] = BASE.BehavioralOutcome


class OfflineMaintenanceOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency) or
    chronic offline maintenance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.OfflineMaintenanceOutcome
    class_class_curie: ClassVar[str] = "base:OfflineMaintenanceOutcome"
    class_name: ClassVar[str] = "offline maintenance outcome"
    class_model_uri: ClassVar[URIRef] = BASE.OfflineMaintenanceOutcome


class TerminationOutcome(YAMLRoot):
    """
    An outcome of termination from resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.TerminationOutcome
    class_class_curie: ClassVar[str] = "base:TerminationOutcome"
    class_name: ClassVar[str] = "termination outcome"
    class_model_uri: ClassVar[URIRef] = BASE.TerminationOutcome


class EpidemiologicalOutcome(YAMLRoot):
    """
    An epidemiological outcome, such as societal fault burden, resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EpidemiologicalOutcome
    class_class_curie: ClassVar[str] = "base:EpidemiologicalOutcome"
    class_name: ClassVar[str] = "epidemiological outcome"
    class_model_uri: ClassVar[URIRef] = BASE.EpidemiologicalOutcome


class SocioeconomicOutcome(YAMLRoot):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure
    event
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SocioeconomicOutcome
    class_class_curie: ClassVar[str] = "base:SocioeconomicOutcome"
    class_name: ClassVar[str] = "socioeconomic outcome"
    class_model_uri: ClassVar[URIRef] = BASE.SocioeconomicOutcome


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.Association
    class_class_curie: ClassVar[str] = "base:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = BASE.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    has_evidence: Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]] = empty_list()
    knowledge_source: Optional[Union[str, InformationResourceId]] = None
    primary_knowledge_source: Optional[Union[str, InformationResourceId]] = None
    aggregator_knowledge_source: Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None
    type: Optional[str] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if not isinstance(self.has_evidence, list):
            self.has_evidence = [self.has_evidence] if self.has_evidence is not None else []
        self.has_evidence = [v if isinstance(v, EvidenceTypeId) else EvidenceTypeId(v) for v in self.has_evidence]

        if self.knowledge_source is not None and not isinstance(self.knowledge_source, InformationResourceId):
            self.knowledge_source = InformationResourceId(self.knowledge_source)

        if self.primary_knowledge_source is not None and not isinstance(self.primary_knowledge_source, InformationResourceId):
            self.primary_knowledge_source = InformationResourceId(self.primary_knowledge_source)

        if not isinstance(self.aggregator_knowledge_source, list):
            self.aggregator_knowledge_source = [self.aggregator_knowledge_source] if self.aggregator_knowledge_source is not None else []
        self.aggregator_knowledge_source = [v if isinstance(v, InformationResourceId) else InformationResourceId(v) for v in self.aggregator_knowledge_source]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        super().__post_init__(**kwargs)


@dataclass
class ControlEntityAssessesNamedThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlEntityAssessesNamedThingAssociation
    class_class_curie: ClassVar[str] = "base:ControlEntityAssessesNamedThingAssociation"
    class_name: ClassVar[str] = "control entity assesses named thing association"
    class_model_uri: ClassVar[URIRef] = BASE.ControlEntityAssessesNamedThingAssociation

    id: Union[str, ControlEntityAssessesNamedThingAssociationId] = None
    subject: Union[str, ControlEntityId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlEntityAssessesNamedThingAssociationId):
            self.id = ControlEntityAssessesNamedThingAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ControlEntityId):
            self.subject = ControlEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ContributorAssociation
    class_class_curie: ClassVar[str] = "base:ContributorAssociation"
    class_name: ClassVar[str] = "contributor association"
    class_model_uri: ClassVar[URIRef] = BASE.ContributorAssociation

    id: Union[str, ContributorAssociationId] = None
    subject: Union[str, InformationContentEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, AgentId] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorAssociationId):
            self.id = ContributorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, InformationContentEntityId):
            self.subject = InformationContentEntityId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AgentId):
            self.object = AgentId(self.object)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        super().__post_init__(**kwargs)


@dataclass
class ServiceTypeToServiceTypePartAssociation(Association):
    """
    Any association between one service type and a service type entity that is a subset of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ServiceTypeToServiceTypePartAssociation
    class_class_curie: ClassVar[str] = "base:ServiceTypeToServiceTypePartAssociation"
    class_name: ClassVar[str] = "service type to service type part association"
    class_model_uri: ClassVar[URIRef] = BASE.ServiceTypeToServiceTypePartAssociation

    id: Union[str, ServiceTypeToServiceTypePartAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceTypeId] = None
    object: Union[str, ServiceTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceTypeToServiceTypePartAssociationId):
            self.id = ServiceTypeToServiceTypePartAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceTypeId):
            self.subject = ServiceTypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ServiceTypeId):
            self.object = ServiceTypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceTypeToClassAssociation(Association):
    """
    Any association between a service type and a class. The service type have have multiple variants in that class or
    a single one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ServiceTypeToClassAssociation
    class_class_curie: ClassVar[str] = "base:ServiceTypeToClassAssociation"
    class_name: ClassVar[str] = "service type to class association"
    class_model_uri: ClassVar[URIRef] = BASE.ServiceTypeToClassAssociation

    id: Union[str, ServiceTypeToClassAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceTypeId] = None
    object: Union[str, ClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceTypeToClassAssociationId):
            self.id = ServiceTypeToClassAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceTypeId):
            self.subject = ServiceTypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ClassId):
            self.object = ClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ClassToClassAssociation(Association):
    """
    abstract parent class for different kinds of class-class or subclasses to subclasses relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassToClassAssociation
    class_class_curie: ClassVar[str] = "base:ClassToClassAssociation"
    class_name: ClassVar[str] = "class to class association"
    class_model_uri: ClassVar[URIRef] = BASE.ClassToClassAssociation

    id: Union[str, ClassToClassAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ClassOrSubclasses] = None
    object: Union[dict, ClassOrSubclasses] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ClassOrSubclasses):
            self.object = ClassOrSubclasses(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToEntityAssociationMixin(YAMLRoot):
    """
    An relationship between a component type and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ComponentTypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:ComponentTypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "component type to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.ComponentTypeToEntityAssociationMixin

    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ControlEntityToEntityAssociationMixin(YAMLRoot):
    """
    An interaction between a control entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlEntityToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:ControlEntityToEntityAssociationMixin"
    class_name: ClassVar[str] = "control entity to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.ControlEntityToEntityAssociationMixin

    subject: Union[dict, ControlEntityOrClassOrSubclasses] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ControlEntityOrClassOrSubclasses):
            self.subject = ControlEntityOrClassOrSubclasses()

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationToEntityAssociationMixin(ControlEntityToEntityAssociationMixin):
    """
    An interaction between a administrative operation and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AdministrativeOperationToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:AdministrativeOperationToEntityAssociationMixin"
    class_name: ClassVar[str] = "administrative operation to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.AdministrativeOperationToEntityAssociationMixin

    subject: Union[str, AdministrativeOperationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AdministrativeOperationId):
            self.subject = AdministrativeOperationId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ControlToEntityAssociationMixin(ControlEntityToEntityAssociationMixin):
    """
    An interaction between a control entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:ControlToEntityAssociationMixin"
    class_name: ClassVar[str] = "control to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.ControlToEntityAssociationMixin

    subject: Union[dict, ControlEntityOrClassOrSubclasses] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ControlEntityOrClassOrSubclasses):
            self.subject = ControlEntityOrClassOrSubclasses()

        super().__post_init__(**kwargs)


@dataclass
class CaseToEntityAssociationMixin(YAMLRoot):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.CaseToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:CaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "case to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.CaseToEntityAssociationMixin

    subject: Union[str, CaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ControlToControlAssociation(Association):
    """
    A relationship between two control entities. This can encompass actual interactions as well as temporal causal
    edges, e.g. one control converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlToControlAssociation
    class_class_curie: ClassVar[str] = "base:ControlToControlAssociation"
    class_name: ClassVar[str] = "control to control association"
    class_model_uri: ClassVar[URIRef] = BASE.ControlToControlAssociation

    id: Union[str, ControlToControlAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ControlEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlToControlAssociationId):
            self.id = ControlToControlAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ControlEntityId):
            self.object = ControlEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ReactionToParticipantAssociation(ControlToControlAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ReactionToParticipantAssociation
    class_class_curie: ClassVar[str] = "base:ReactionToParticipantAssociation"
    class_name: ClassVar[str] = "reaction to participant association"
    class_model_uri: ClassVar[URIRef] = BASE.ReactionToParticipantAssociation

    id: Union[str, ReactionToParticipantAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ControlEntityId] = None
    subject: Union[str, OperationalEntityId] = None
    ratios: Optional[int] = None
    reaction_direction: Optional[Union[str, "ReactionDirectionEnum"]] = None
    reaction_side: Optional[Union[str, "ReactionSideEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionToParticipantAssociationId):
            self.id = ReactionToParticipantAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self.ratios is not None and not isinstance(self.ratios, int):
            self.ratios = int(self.ratios)

        if self.reaction_direction is not None and not isinstance(self.reaction_direction, ReactionDirectionEnum):
            self.reaction_direction = ReactionDirectionEnum(self.reaction_direction)

        if self.reaction_side is not None and not isinstance(self.reaction_side, ReactionSideEnum):
            self.reaction_side = ReactionSideEnum(self.reaction_side)

        super().__post_init__(**kwargs)


@dataclass
class ReactionToCatalystAssociation(ReactionToParticipantAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ReactionToCatalystAssociation
    class_class_curie: ClassVar[str] = "base:ReactionToCatalystAssociation"
    class_name: ClassVar[str] = "reaction to catalyst association"
    class_model_uri: ClassVar[URIRef] = BASE.ReactionToCatalystAssociation

    id: Union[str, ReactionToCatalystAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, OperationalEntityId] = None
    object: Union[dict, ClassOrSubclasses] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionToCatalystAssociationId):
            self.id = ReactionToCatalystAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ClassOrSubclasses):
            self.object = ClassOrSubclasses(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ControlToFaultOrObservableFeatureAssociation(Association):
    """
    An interaction between a control entity and a observable feature or fault, where the presence of the control gives
    rise to or exacerbates the observable feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlToFaultOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:ControlToFaultOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "control to fault or observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.ControlToFaultOrObservableFeatureAssociation

    id: Union[str, ControlToFaultOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, FaultOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlToFaultOrObservableFeatureAssociationId):
            self.id = ControlToFaultOrObservableFeatureAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, FaultOrObservableFeatureId):
            self.object = FaultOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ClassToPathwayAssociation(Association):
    """
    An interaction between a class or subclasses and a computational process or pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassToPathwayAssociation
    class_class_curie: ClassVar[str] = "base:ClassToPathwayAssociation"
    class_name: ClassVar[str] = "class to pathway association"
    class_model_uri: ClassVar[URIRef] = BASE.ClassToPathwayAssociation

    id: Union[str, ClassToPathwayAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ClassOrSubclasses] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassToPathwayAssociationId):
            self.id = ClassToPathwayAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OperationalActivityToPathwayAssociation(Association):
    """
    Association that holds the relationship between a operational activity and the pathway it participates in.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.OperationalActivityToPathwayAssociation
    class_class_curie: ClassVar[str] = "base:OperationalActivityToPathwayAssociation"
    class_name: ClassVar[str] = "operational activity to pathway association"
    class_model_uri: ClassVar[URIRef] = BASE.OperationalActivityToPathwayAssociation

    id: Union[str, OperationalActivityToPathwayAssociationId] = None
    subject: Union[str, OperationalActivityId] = None
    object: Union[str, PathwayId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalActivityToPathwayAssociationId):
            self.id = OperationalActivityToPathwayAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OperationalActivityId):
            self.subject = OperationalActivityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ControlToPathwayAssociation(Association):
    """
    An interaction between a control entity and a computational process or pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControlToPathwayAssociation
    class_class_curie: ClassVar[str] = "base:ControlToPathwayAssociation"
    class_name: ClassVar[str] = "control to pathway association"
    class_model_uri: ClassVar[URIRef] = BASE.ControlToPathwayAssociation

    id: Union[str, ControlToPathwayAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ControlEntityId] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlToPathwayAssociationId):
            self.id = ControlToPathwayAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ControlEntityId):
            self.subject = ControlEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationToClassAssociation(Association):
    """
    An interaction between a administrative operation and a class or subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AdministrativeOperationToClassAssociation
    class_class_curie: ClassVar[str] = "base:AdministrativeOperationToClassAssociation"
    class_name: ClassVar[str] = "administrative operation to class association"
    class_model_uri: ClassVar[URIRef] = BASE.AdministrativeOperationToClassAssociation

    id: Union[str, AdministrativeOperationToClassAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, ClassOrSubclasses] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationToClassAssociationId):
            self.id = AdministrativeOperationToClassAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ClassOrSubclasses):
            self.object = ClassOrSubclasses(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class FaultToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:FaultToEntityAssociationMixin"
    class_name: ClassVar[str] = "fault to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.FaultToEntityAssociationMixin

    subject: Union[str, FaultId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, FaultId):
            self.subject = FaultId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EntityToExposureEventAssociationMixin(YAMLRoot):
    """
    An association between some entity and an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToExposureEventAssociationMixin
    class_class_curie: ClassVar[str] = "base:EntityToExposureEventAssociationMixin"
    class_name: ClassVar[str] = "entity to exposure event association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToExposureEventAssociationMixin

    object: Union[str, ExposureEventId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ExposureEventId):
            self.object = ExposureEventId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class FaultToExposureEventAssociation(Association):
    """
    An association between an exposure event and a fault.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultToExposureEventAssociation
    class_class_curie: ClassVar[str] = "base:FaultToExposureEventAssociation"
    class_name: ClassVar[str] = "fault to exposure event association"
    class_model_uri: ClassVar[URIRef] = BASE.FaultToExposureEventAssociation

    id: Union[str, FaultToExposureEventAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultToExposureEventAssociationId):
            self.id = FaultToExposureEventAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EntityToOutcomeAssociationMixin(YAMLRoot):
    """
    An association between some entity and an outcome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToOutcomeAssociationMixin
    class_class_curie: ClassVar[str] = "base:EntityToOutcomeAssociationMixin"
    class_name: ClassVar[str] = "entity to outcome association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToOutcomeAssociationMixin

    object: Union[dict, Outcome] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Outcome):
            self.object = Outcome()

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToOutcomeAssociation(Association):
    """
    An association between an exposure event and an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ExposureEventToOutcomeAssociation
    class_class_curie: ClassVar[str] = "base:ExposureEventToOutcomeAssociation"
    class_name: ClassVar[str] = "exposure event to outcome association"
    class_model_uri: ClassVar[URIRef] = BASE.ExposureEventToOutcomeAssociation

    id: Union[str, ExposureEventToOutcomeAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    population_context_qualifier: Optional[Union[str, PopulationOfIndividualSystemsId]] = None
    temporal_context_qualifier: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventToOutcomeAssociationId):
            self.id = ExposureEventToOutcomeAssociationId(self.id)

        if self.population_context_qualifier is not None and not isinstance(self.population_context_qualifier, PopulationOfIndividualSystemsId):
            self.population_context_qualifier = PopulationOfIndividualSystemsId(self.population_context_qualifier)

        if self.temporal_context_qualifier is not None and not isinstance(self.temporal_context_qualifier, TimeType):
            self.temporal_context_qualifier = TimeType(self.temporal_context_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class FrequencyQualifierMixin(YAMLRoot):
    """
    Qualifier for frequency type associations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FrequencyQualifierMixin
    class_class_curie: ClassVar[str] = "base:FrequencyQualifierMixin"
    class_name: ClassVar[str] = "frequency qualifier mixin"
    class_model_uri: ClassVar[URIRef] = BASE.FrequencyQualifierMixin

    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFeatureOrFaultQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to fault or observable feature associations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToFeatureOrFaultQualifiersMixin
    class_class_curie: ClassVar[str] = "base:EntityToFeatureOrFaultQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or fault qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToFeatureOrFaultQualifiersMixin

    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToObservableFeatureAssociationMixin(EntityToFeatureOrFaultQualifiersMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "base:EntityToObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToObservableFeatureAssociationMixin

    object: Union[str, ObservableFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ObservableFeatureId):
            self.object = ObservableFeatureId(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntityToNamedThingAssociation(Association):
    """
    association between a named thing and a information content entity where the specific context of the relationship
    between that named thing and the publication is unknown. For example, model system databases often capture the
    knowledge that a named thing is found in a journal article, but not specifically the context in which that named
    thing was documented in the article. In these cases, this association with the accompanying predicate 'mentions'
    could be used. Conversely, for more specific associations (like 'named thing to fault association', the
    publication should be captured as an edge property).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.InformationContentEntityToNamedThingAssociation
    class_class_curie: ClassVar[str] = "base:InformationContentEntityToNamedThingAssociation"
    class_name: ClassVar[str] = "information content entity to named thing association"
    class_model_uri: ClassVar[URIRef] = BASE.InformationContentEntityToNamedThingAssociation

    id: Union[str, InformationContentEntityToNamedThingAssociationId] = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationContentEntityToNamedThingAssociationId):
            self.id = InformationContentEntityToNamedThingAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFaultAssociationMixin(EntityToFeatureOrFaultQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a fault
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToFaultAssociationMixin
    class_class_curie: ClassVar[str] = "base:EntityToFaultAssociationMixin"
    class_name: ClassVar[str] = "entity to fault association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToFaultAssociationMixin

    object: Union[str, FaultId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, FaultId):
            self.object = FaultId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class FaultOrObservableFeatureToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:FaultOrObservableFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "fault or observable feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureToEntityAssociationMixin

    subject: Union[str, FaultOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, FaultOrObservableFeatureId):
            self.subject = FaultOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class FaultOrObservableFeatureToLocationAssociation(Association):
    """
    An association between either a fault or a observable feature and an named thing, where the fault/feature
    manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureToLocationAssociation
    class_class_curie: ClassVar[str] = "base:FaultOrObservableFeatureToLocationAssociation"
    class_name: ClassVar[str] = "fault or observable feature to location association"
    class_model_uri: ClassVar[URIRef] = BASE.FaultOrObservableFeatureToLocationAssociation

    id: Union[str, FaultOrObservableFeatureToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultOrObservableFeatureToLocationAssociationId):
            self.id = FaultOrObservableFeatureToLocationAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFaultOrObservableFeatureAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToFaultOrObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "base:EntityToFaultOrObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to fault or observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToFaultOrObservableFeatureAssociationMixin

    object: Union[str, FaultOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, FaultOrObservableFeatureId):
            self.object = FaultOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceTypeToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ServiceTypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:ServiceTypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "service type to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.ServiceTypeToEntityAssociationMixin

    subject: Union[str, ServiceTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceTypeId):
            self.subject = ServiceTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceTypeToObservableFeatureAssociation(Association):
    """
    Any association between one service type and a observable feature, where having the service type confers the
    observable feature, either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ServiceTypeToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:ServiceTypeToObservableFeatureAssociation"
    class_name: ClassVar[str] = "service type to observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.ServiceTypeToObservableFeatureAssociation

    id: Union[str, ServiceTypeToObservableFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceTypeId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceTypeToObservableFeatureAssociationId):
            self.id = ServiceTypeToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceTypeId):
            self.subject = ServiceTypeId(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToObservableFeatureAssociation(Association):
    """
    Any association between an environment and a observable feature, where being in the environment influences the
    observable feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ExposureEventToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:ExposureEventToObservableFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.ExposureEventToObservableFeatureAssociation

    id: Union[str, ExposureEventToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, ExposureEventId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventToObservableFeatureAssociationId):
            self.id = ExposureEventToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExposureEventId):
            self.subject = ExposureEventId(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class FaultToObservableFeatureAssociation(Association):
    """
    An association between a fault and a observable feature in which the observable feature is associated with the
    fault in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FaultToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:FaultToObservableFeatureAssociation"
    class_name: ClassVar[str] = "fault to observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.FaultToObservableFeatureAssociation

    id: Union[str, FaultToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, FaultId] = None
    object: Union[str, ObservableFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultToObservableFeatureAssociationId):
            self.id = FaultToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, FaultId):
            self.subject = FaultId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ObservableFeatureId):
            self.object = ObservableFeatureId(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class CaseToObservableFeatureAssociation(Association):
    """
    An association between a case (e.g. individual element) and a observable feature in which the element has or has
    had the observable feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.CaseToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:CaseToObservableFeatureAssociation"
    class_name: ClassVar[str] = "case to observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.CaseToObservableFeatureAssociation

    id: Union[str, CaseToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseToObservableFeatureAssociationId):
            self.id = CaseToObservableFeatureAssociationId(self.id)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class BehaviorToBehavioralFeatureAssociation(Association):
    """
    An association between an aggregate behavior and a behavioral feature manifested by the element exhibited or has
    exhibited the behavior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.BehaviorToBehavioralFeatureAssociation
    class_class_curie: ClassVar[str] = "base:BehaviorToBehavioralFeatureAssociation"
    class_name: ClassVar[str] = "behavior to behavioral feature association"
    class_model_uri: ClassVar[URIRef] = BASE.BehaviorToBehavioralFeatureAssociation

    id: Union[str, BehaviorToBehavioralFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, BehaviorId] = None
    object: Union[str, BehavioralFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorToBehavioralFeatureAssociationId):
            self.id = BehaviorToBehavioralFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, BehaviorId):
            self.subject = BehaviorId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BehavioralFeatureId):
            self.object = BehavioralFeatureId(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ClassToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:ClassToEntityAssociationMixin"
    class_name: ClassVar[str] = "class to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.ClassToEntityAssociationMixin

    subject: Union[dict, ClassOrSubclasses] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class ClassToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:ClassToObservableFeatureAssociation"
    class_name: ClassVar[str] = "class to observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.ClassToObservableFeatureAssociation

    id: Union[str, ClassToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ClassOrSubclasses] = None
    object: Union[str, ObservableFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassToObservableFeatureAssociationId):
            self.id = ClassToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ObservableFeatureId):
            self.object = ObservableFeatureId(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ClassToFaultAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassToFaultAssociation
    class_class_curie: ClassVar[str] = "base:ClassToFaultAssociation"
    class_name: ClassVar[str] = "class to fault association"
    class_model_uri: ClassVar[URIRef] = BASE.ClassToFaultAssociation

    id: Union[str, ClassToFaultAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ClassOrSubclasses] = None
    object: Union[str, FaultId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassToFaultAssociationId):
            self.id = ClassToFaultAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, FaultId):
            self.object = FaultId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ControllableClassToFaultAssociation(ClassToFaultAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ControllableClassToFaultAssociation
    class_class_curie: ClassVar[str] = "base:ControllableClassToFaultAssociation"
    class_name: ClassVar[str] = "controllable class to fault association"
    class_model_uri: ClassVar[URIRef] = BASE.ControllableClassToFaultAssociation

    id: Union[str, ControllableClassToFaultAssociationId] = None
    object: Union[str, FaultId] = None
    subject: Union[dict, ClassOrSubclasses] = None
    predicate: Union[str, PredicateType] = None
    has_evidence: Optional[Union[Union[str, "ControllableClassCategoryEnum"], List[Union[str, "ControllableClassCategoryEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControllableClassToFaultAssociationId):
            self.id = ControllableClassToFaultAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if not isinstance(self.has_evidence, list):
            self.has_evidence = [self.has_evidence] if self.has_evidence is not None else []
        self.has_evidence = [v if isinstance(v, ControllableClassCategoryEnum) else ControllableClassCategoryEnum(v) for v in self.has_evidence]

        super().__post_init__(**kwargs)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.PopulationToPopulationAssociation
    class_class_curie: ClassVar[str] = "base:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = BASE.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    subject: Union[str, PopulationOfIndividualSystemsId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, PopulationOfIndividualSystemsId):
            self.subject = PopulationOfIndividualSystemsId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ServiceTypeToFaultAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ServiceTypeToFaultAssociation
    class_class_curie: ClassVar[str] = "base:ServiceTypeToFaultAssociation"
    class_name: ClassVar[str] = "service type to fault association"
    class_model_uri: ClassVar[URIRef] = BASE.ServiceTypeToFaultAssociation

    id: Union[str, ServiceTypeToFaultAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceTypeToFaultAssociationId):
            self.id = ServiceTypeToFaultAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class SystemToSystemAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SystemToSystemAssociation
    class_class_curie: ClassVar[str] = "base:SystemToSystemAssociation"
    class_name: ClassVar[str] = "system to system association"
    class_model_uri: ClassVar[URIRef] = BASE.SystemToSystemAssociation

    id: Union[str, SystemToSystemAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, IndividualSystemId] = None
    object: Union[str, IndividualSystemId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemToSystemAssociationId):
            self.id = SystemToSystemAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, IndividualSystemId):
            self.subject = IndividualSystemId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, IndividualSystemId):
            self.object = IndividualSystemId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class TaxonToTaxonAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.TaxonToTaxonAssociation
    class_class_curie: ClassVar[str] = "base:TaxonToTaxonAssociation"
    class_name: ClassVar[str] = "taxon to taxon association"
    class_model_uri: ClassVar[URIRef] = BASE.TaxonToTaxonAssociation

    id: Union[str, TaxonToTaxonAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, SystemTaxonId] = None
    object: Union[str, SystemTaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonToTaxonAssociationId):
            self.id = TaxonToTaxonAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SystemTaxonId):
            self.subject = SystemTaxonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, SystemTaxonId):
            self.object = SystemTaxonId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ClassToExpressionSiteAssociation(Association):
    """
    An association between a class and an expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.ClassToExpressionSiteAssociation
    class_class_curie: ClassVar[str] = "base:ClassToExpressionSiteAssociation"
    class_name: ClassVar[str] = "class to expression site association"
    class_model_uri: ClassVar[URIRef] = BASE.ClassToExpressionSiteAssociation

    id: Union[str, ClassToExpressionSiteAssociationId] = None
    subject: Union[dict, ClassOrSubclasses] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassToExpressionSiteAssociationId):
            self.id = ClassToExpressionSiteAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ClassOrSubclasses):
            self.subject = ClassOrSubclasses(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a assembly mixin (class, subclasses, or complex of subclasses) and either a operational
    activity, a computational process or a component location in which a function is executed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.FunctionalAssociation
    class_class_curie: ClassVar[str] = "base:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = BASE.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, AssemblyMixin] = None
    object: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AssemblyMixin):
            self.subject = AssemblyMixin(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OntologyClassId):
            self.object = OntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AssemblyToEntityAssociationMixin(YAMLRoot):
    """
    an association which has a assembly mixin mixin as a subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AssemblyToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "base:AssemblyToEntityAssociationMixin"
    class_name: ClassVar[str] = "assembly to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BASE.AssemblyToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class AssemblyToOperationalActivityAssociation(FunctionalAssociation):
    """
    A functional association between a assembly (class, subclasses or complex) and a operational activity where the
    entity carries out the activity, or contributes to its execution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AssemblyToOperationalActivityAssociation
    class_class_curie: ClassVar[str] = "base:AssemblyToOperationalActivityAssociation"
    class_name: ClassVar[str] = "assembly to operational activity association"
    class_model_uri: ClassVar[URIRef] = BASE.AssemblyToOperationalActivityAssociation

    id: Union[str, AssemblyToOperationalActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, AssemblyMixin] = None
    object: Union[str, OperationalActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssemblyToOperationalActivityAssociationId):
            self.id = AssemblyToOperationalActivityAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OperationalActivityId):
            self.object = OperationalActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AssemblyToComputationalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a assembly (class, subclasses or complex) and a computational process or pathway
    where the entity carries out some part of the process, regulates it, or acts upstream of it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AssemblyToComputationalProcessAssociation
    class_class_curie: ClassVar[str] = "base:AssemblyToComputationalProcessAssociation"
    class_name: ClassVar[str] = "assembly to computational process association"
    class_model_uri: ClassVar[URIRef] = BASE.AssemblyToComputationalProcessAssociation

    id: Union[str, AssemblyToComputationalProcessAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, AssemblyMixin] = None
    object: Union[str, ComputationalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssemblyToComputationalProcessAssociationId):
            self.id = AssemblyToComputationalProcessAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComputationalProcessId):
            self.object = ComputationalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AssemblyToComponentAssociation(FunctionalAssociation):
    """
    A functional association between a assembly (class, subclasses or complex) and a component where the entity
    carries out its function in the component.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.AssemblyToComponentAssociation
    class_class_curie: ClassVar[str] = "base:AssemblyToComponentAssociation"
    class_name: ClassVar[str] = "assembly to component association"
    class_model_uri: ClassVar[URIRef] = BASE.AssemblyToComponentAssociation

    id: Union[str, AssemblyToComponentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, AssemblyMixin] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssemblyToComponentAssociationId):
            self.id = AssemblyToComponentAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFaultAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToFaultAssociation
    class_class_curie: ClassVar[str] = "base:EntityToFaultAssociation"
    class_name: ClassVar[str] = "entity to fault association"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToFaultAssociation

    id: Union[str, EntityToFaultAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    regulator_approval_status: Optional[Union[str, "RegulatorApprovalStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityToFaultAssociationId):
            self.id = EntityToFaultAssociationId(self.id)

        if self.regulator_approval_status is not None and not isinstance(self.regulator_approval_status, RegulatorApprovalStatusEnum):
            self.regulator_approval_status = RegulatorApprovalStatusEnum(self.regulator_approval_status)

        super().__post_init__(**kwargs)


@dataclass
class EntityToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.EntityToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "base:EntityToObservableFeatureAssociation"
    class_name: ClassVar[str] = "entity to observable feature association"
    class_model_uri: ClassVar[URIRef] = BASE.EntityToObservableFeatureAssociation

    id: Union[str, EntityToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    regulator_approval_status: Optional[Union[str, "RegulatorApprovalStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityToObservableFeatureAssociationId):
            self.id = EntityToObservableFeatureAssociationId(self.id)

        if self.regulator_approval_status is not None and not isinstance(self.regulator_approval_status, RegulatorApprovalStatusEnum):
            self.regulator_approval_status = RegulatorApprovalStatusEnum(self.regulator_approval_status)

        super().__post_init__(**kwargs)


@dataclass
class SystemTaxonToEntityAssociation(YAMLRoot):
    """
    An association between an system taxon and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BASE.SystemTaxonToEntityAssociation
    class_class_curie: ClassVar[str] = "base:SystemTaxonToEntityAssociation"
    class_name: ClassVar[str] = "system taxon to entity association"
    class_model_uri: ClassVar[URIRef] = BASE.SystemTaxonToEntityAssociation

    subject: Union[str, SystemTaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SystemTaxonId):
            self.subject = SystemTaxonId(self.subject)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(text="ALIVE",
                                 description="the person is living",
                                 meaning=PATO["0001421"])
    DEAD = PermissibleValue(text="DEAD",
                               description="the person is deceased",
                               meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(text="UNKNOWN",
                                     description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

class DirectionQualifierEnum(EnumDefinitionImpl):

    increased = PermissibleValue(text="increased")
    upregulated = PermissibleValue(text="upregulated")
    decreased = PermissibleValue(text="decreased")
    downregulated = PermissibleValue(text="downregulated")

    _defn = EnumDefinition(
        name="DirectionQualifierEnum",
    )

class LogicalInterpretationEnum(EnumDefinitionImpl):

    some_some = PermissibleValue(text="some_some",
                                         description="A modifier on a triple that causes the triple to be interpreted as a some-some statement",
                                         meaning=OS.SomeSomeInterpretation)
    all_some = PermissibleValue(text="all_some",
                                       description="A modifier on a triple that causes the triple to be interpreted as an all-some statement.",
                                       meaning=OS.AllSomeInterpretation)
    inverse_all_some = PermissibleValue(text="inverse_all_some")

    _defn = EnumDefinition(
        name="LogicalInterpretationEnum",
    )

class ReactionDirectionEnum(EnumDefinitionImpl):

    left_to_right = PermissibleValue(text="left_to_right")
    right_to_left = PermissibleValue(text="right_to_left")
    bidirectional = PermissibleValue(text="bidirectional")
    neutral = PermissibleValue(text="neutral")

    _defn = EnumDefinition(
        name="ReactionDirectionEnum",
    )

class ReactionSideEnum(EnumDefinitionImpl):

    left = PermissibleValue(text="left")
    right = PermissibleValue(text="right")

    _defn = EnumDefinition(
        name="ReactionSideEnum",
    )

class PhaseEnum(EnumDefinitionImpl):
    """
    Phase type
    """
    _defn = EnumDefinition(
        name="PhaseEnum",
        description="Phase type",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0") )
        setattr(cls, "1",
                PermissibleValue(text="1") )
        setattr(cls, "2",
                PermissibleValue(text="2") )

class SequenceEnum(EnumDefinitionImpl):
    """
    Sequence type
    """
    _defn = EnumDefinition(
        name="SequenceEnum",
        description="Sequence type",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0") )
        setattr(cls, "1",
                PermissibleValue(text="1") )
        setattr(cls, "2",
                PermissibleValue(text="2") )

class DeliveryEnum(EnumDefinitionImpl):
    """
    Delivery type
    """
    _defn = EnumDefinition(
        name="DeliveryEnum",
        description="Delivery type",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0") )
        setattr(cls, "1",
                PermissibleValue(text="1") )
        setattr(cls, "2",
                PermissibleValue(text="2") )

class ControllableClassCategoryEnum(EnumDefinitionImpl):
    """
    Controllable classes
    """
    _defn = EnumDefinition(
        name="ControllableClassCategoryEnum",
        description="Controllable classes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0") )
        setattr(cls, "1",
                PermissibleValue(text="1") )
        setattr(cls, "2",
                PermissibleValue(text="2") )

class RegulatorApprovalStatusEnum(EnumDefinitionImpl):
    """
    Regulator appoval status types
    """
    a = PermissibleValue(text="a")
    b = PermissibleValue(text="b")
    c = PermissibleValue(text="c")

    _defn = EnumDefinition(
        name="RegulatorApprovalStatusEnum",
        description="Regulator appoval status types",
    )

class RegulatorGuidelineEventEnum(EnumDefinitionImpl):
    """
    "please consult with the Regulator guidelines as proposed in this document,
    https://example.com/regulator.io/guideline"
    """
    _defn = EnumDefinition(
        name="RegulatorGuidelineEventEnum",
        description="\"please consult with the Regulator guidelines as proposed in this document, https://example.com/regulator.io/guideline\"",
    )

class RegulatorAdverseEventEnum(EnumDefinitionImpl):
    """
    please consult with the Regulator guidelines.
    """
    _defn = EnumDefinition(
        name="RegulatorAdverseEventEnum",
        description="please consult with the Regulator guidelines.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0") )
        setattr(cls, "1",
                PermissibleValue(text="1") )

# Slots
class slots:
    pass

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=BASE.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=BASE.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=BASE.age_in_years, name="age_in_years", curie=BASE.curie('age_in_years'),
                   model_uri=BASE.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=BASE.vital_status, name="vital_status", curie=BASE.curie('vital_status'),
                   model_uri=BASE.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.has_attribute = Slot(uri=BASE.has_attribute, name="has attribute", curie=BASE.curie('has_attribute'),
                   model_uri=BASE.has_attribute, domain=Entity, range=Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]])

slots.has_attribute_type = Slot(uri=BASE.has_attribute_type, name="has attribute type", curie=BASE.curie('has_attribute_type'),
                   model_uri=BASE.has_attribute_type, domain=Attribute, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=BASE.has_qualitative_value, name="has qualitative value", curie=BASE.curie('has_qualitative_value'),
                   model_uri=BASE.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=BASE.has_quantitative_value, name="has quantitative value", curie=BASE.curie('has_quantitative_value'),
                   model_uri=BASE.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=BASE.has_numeric_value, name="has numeric value", curie=BASE.curie('has_numeric_value'),
                   model_uri=BASE.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_unit = Slot(uri=BASE.has_unit, name="has unit", curie=BASE.curie('has_unit'),
                   model_uri=BASE.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.base_coordinate = Slot(uri=BASE.base_coordinate, name="base coordinate", curie=BASE.curie('base_coordinate'),
                   model_uri=BASE.base_coordinate, domain=NamedThing, range=Optional[int])

slots.node_property = Slot(uri=BASE.node_property, name="node property", curie=BASE.curie('node_property'),
                   model_uri=BASE.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=BASE.id, name="id", curie=BASE.curie('id'),
                   model_uri=BASE.id, domain=None, range=URIRef)

slots.iri = Slot(uri=BASE.iri, name="iri", curie=BASE.curie('iri'),
                   model_uri=BASE.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=BASE.type, domain=None, range=Optional[str])

slots.category = Slot(uri=BASE.category, name="category", curie=BASE.curie('category'),
                   model_uri=BASE.category, domain=Entity, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=BASE.name, domain=None, range=Optional[Union[str, LabelType]])

slots.ratios = Slot(uri=BASE.ratios, name="ratios", curie=BASE.curie('ratios'),
                   model_uri=BASE.ratios, domain=Association, range=Optional[int])

slots.reaction_direction = Slot(uri=BASE.reaction_direction, name="reaction direction", curie=BASE.curie('reaction_direction'),
                   model_uri=BASE.reaction_direction, domain=Association, range=Optional[Union[str, "ReactionDirectionEnum"]])

slots.reaction_balanced = Slot(uri=BASE.reaction_balanced, name="reaction balanced", curie=BASE.curie('reaction_balanced'),
                   model_uri=BASE.reaction_balanced, domain=Association, range=Optional[Union[bool, Bool]])

slots.reaction_side = Slot(uri=BASE.reaction_side, name="reaction side", curie=BASE.curie('reaction_side'),
                   model_uri=BASE.reaction_side, domain=Association, range=Optional[Union[str, "ReactionSideEnum"]])

slots.symbol = Slot(uri=BASE.symbol, name="symbol", curie=BASE.curie('symbol'),
                   model_uri=BASE.symbol, domain=NamedThing, range=Optional[str])

slots.synonym = Slot(uri=BASE.synonym, name="synonym", curie=BASE.curie('synonym'),
                   model_uri=BASE.synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.exact_synonym = Slot(uri=BASE.exact_synonym, name="exact_synonym", curie=BASE.curie('exact_synonym'),
                   model_uri=BASE.exact_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.broad_synonym = Slot(uri=BASE.broad_synonym, name="broad_synonym", curie=BASE.curie('broad_synonym'),
                   model_uri=BASE.broad_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.narrow_synonym = Slot(uri=BASE.narrow_synonym, name="narrow_synonym", curie=BASE.curie('narrow_synonym'),
                   model_uri=BASE.narrow_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.related_synonym = Slot(uri=BASE.related_synonym, name="related_synonym", curie=BASE.curie('related_synonym'),
                   model_uri=BASE.related_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.has_topic = Slot(uri=BASE.has_topic, name="has topic", curie=BASE.curie('has_topic'),
                   model_uri=BASE.has_topic, domain=NamedThing, range=Optional[Union[str, OntologyClassId]])

slots.xref = Slot(uri=BASE.xref, name="xref", curie=BASE.curie('xref'),
                   model_uri=BASE.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.full_name = Slot(uri=BASE.full_name, name="full name", curie=BASE.curie('full_name'),
                   model_uri=BASE.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=BASE.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=BASE.systematic_synonym, name="systematic synonym", curie=BASE.curie('systematic_synonym'),
                   model_uri=BASE.systematic_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.affiliation = Slot(uri=BASE.affiliation, name="affiliation", curie=BASE.curie('affiliation'),
                   model_uri=BASE.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=BASE.address, name="address", curie=BASE.curie('address'),
                   model_uri=BASE.address, domain=NamedThing, range=Optional[str])

slots.latitude = Slot(uri=BASE.latitude, name="latitude", curie=BASE.curie('latitude'),
                   model_uri=BASE.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=BASE.longitude, name="longitude", curie=BASE.curie('longitude'),
                   model_uri=BASE.longitude, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=BASE.timepoint, name="timepoint", curie=BASE.curie('timepoint'),
                   model_uri=BASE.timepoint, domain=None, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=BASE.creation_date, name="creation date", curie=BASE.curie('creation_date'),
                   model_uri=BASE.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=BASE.update_date, name="update date", curie=BASE.curie('update_date'),
                   model_uri=BASE.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.aggregate_statistic = Slot(uri=BASE.aggregate_statistic, name="aggregate statistic", curie=BASE.curie('aggregate_statistic'),
                   model_uri=BASE.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=BASE.has_count, name="has count", curie=BASE.curie('has_count'),
                   model_uri=BASE.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=BASE.has_total, name="has total", curie=BASE.curie('has_total'),
                   model_uri=BASE.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=BASE.has_quotient, name="has quotient", curie=BASE.curie('has_quotient'),
                   model_uri=BASE.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=BASE.has_percentage, name="has percentage", curie=BASE.curie('has_percentage'),
                   model_uri=BASE.has_percentage, domain=NamedThing, range=Optional[float])

slots.has_taxonomic_rank = Slot(uri=BASE.has_taxonomic_rank, name="has taxonomic rank", curie=BASE.curie('has_taxonomic_rank'),
                   model_uri=BASE.has_taxonomic_rank, domain=NamedThing, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.has_dataset = Slot(uri=DCT.source, name="has dataset", curie=DCT.curie('source'),
                   model_uri=BASE.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.source_web_page = Slot(uri=BASE.source_web_page, name="source web page", curie=BASE.curie('source_web_page'),
                   model_uri=BASE.source_web_page, domain=DatasetSummary, range=Optional[str])

slots.source_logo = Slot(uri=SCHEMA.logo, name="source logo", curie=SCHEMA.curie('logo'),
                   model_uri=BASE.source_logo, domain=DatasetSummary, range=Optional[str])

slots.retrieved_on = Slot(uri=BASE.retrieved_on, name="retrieved on", curie=BASE.curie('retrieved_on'),
                   model_uri=BASE.retrieved_on, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=BASE.version_of, name="version of", curie=BASE.curie('version_of'),
                   model_uri=BASE.version_of, domain=DatasetVersion, range=Optional[Union[str, DatasetSummaryId]])

slots.version = Slot(uri=BASE.version, name="version", curie=BASE.curie('version'),
                   model_uri=BASE.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=BASE.license, name="license", curie=BASE.curie('license'),
                   model_uri=BASE.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=BASE.rights, name="rights", curie=BASE.curie('rights'),
                   model_uri=BASE.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=BASE.format, name="format", curie=BASE.curie('format'),
                   model_uri=BASE.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=BASE.created_with, name="created with", curie=BASE.curie('created_with'),
                   model_uri=BASE.created_with, domain=Dataset, range=Optional[str])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download url", curie=DCAT.curie('downloadURL'),
                   model_uri=BASE.download_url, domain=InformationContentEntity, range=Optional[str])

slots.dataset_download_url = Slot(uri=WIKIDATA_PROPERTY.P4945, name="dataset download url", curie=WIKIDATA_PROPERTY.curie('P4945'),
                   model_uri=BASE.dataset_download_url, domain=Dataset, range=Optional[str])

slots.distribution_download_url = Slot(uri=BASE.distribution_download_url, name="distribution download url", curie=BASE.curie('distribution_download_url'),
                   model_uri=BASE.distribution_download_url, domain=DatasetDistribution, range=Optional[str])

slots.ingest_date = Slot(uri=PAV.version, name="ingest date", curie=PAV.curie('version'),
                   model_uri=BASE.ingest_date, domain=DatasetVersion, range=Optional[str])

slots.has_distribution = Slot(uri=DCT.distribution, name="has distribution", curie=DCT.curie('distribution'),
                   model_uri=BASE.has_distribution, domain=DatasetVersion, range=Optional[Union[str, DatasetDistributionId]])

slots.published_in = Slot(uri=BASE.published_in, name="published in", curie=BASE.curie('published_in'),
                   model_uri=BASE.published_in, domain=Publication, range=Optional[Union[str, URIorCURIE]])

slots.iso_abbreviation = Slot(uri=BASE.iso_abbreviation, name="iso abbreviation", curie=BASE.curie('iso_abbreviation'),
                   model_uri=BASE.iso_abbreviation, domain=Publication, range=Optional[str])

slots.authors = Slot(uri=BASE.authors, name="authors", curie=BASE.curie('authors'),
                   model_uri=BASE.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.volume = Slot(uri=BASE.volume, name="volume", curie=BASE.curie('volume'),
                   model_uri=BASE.volume, domain=Publication, range=Optional[str])

slots.chapter = Slot(uri=BASE.chapter, name="chapter", curie=BASE.curie('chapter'),
                   model_uri=BASE.chapter, domain=BookChapter, range=Optional[str])

slots.issue = Slot(uri=BASE.issue, name="issue", curie=BASE.curie('issue'),
                   model_uri=BASE.issue, domain=Publication, range=Optional[str])

slots.pages = Slot(uri=BASE.pages, name="pages", curie=BASE.curie('pages'),
                   model_uri=BASE.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=BASE.summary, name="summary", curie=BASE.curie('summary'),
                   model_uri=BASE.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=BASE.keywords, name="keywords", curie=BASE.curie('keywords'),
                   model_uri=BASE.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcsh_terms = Slot(uri=BASE.lcsh_terms, name="lcsh terms", curie=BASE.curie('lcsh_terms'),
                   model_uri=BASE.lcsh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_computational_sequence = Slot(uri=BASE.has_computational_sequence, name="has computational sequence", curie=BASE.curie('has_computational_sequence'),
                   model_uri=BASE.has_computational_sequence, domain=NamedThing, range=Optional[Union[str, ComputationalSequence]])

slots.has_class_or_subclasses = Slot(uri=BASE.has_class_or_subclasses, name="has class or subclasses", curie=BASE.curie('has_class_or_subclasses'),
                   model_uri=BASE.has_class_or_subclasses, domain=NamedThing, range=Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]])

slots.has_class = Slot(uri=BASE.has_class, name="has class", curie=BASE.curie('has_class'),
                   model_uri=BASE.has_class, domain=NamedThing, range=Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]])

slots.has_homogeneity = Slot(uri=BASE.has_homogeneity, name="has homogeneity", curie=BASE.curie('has_homogeneity'),
                   model_uri=BASE.has_homogeneity, domain=None, range=Optional[Union[str, HomogeneityId]])

slots.has_formula = Slot(uri=BASE.has_formula, name="has formula", curie=BASE.curie('has_formula'),
                   model_uri=BASE.has_formula, domain=NamedThing, range=Optional[str])

slots.is_controller = Slot(uri=BASE.is_controller, name="is controller", curie=BASE.curie('is_controller'),
                   model_uri=BASE.is_controller, domain=OperationalEntity, range=Optional[Union[bool, Bool]])

slots.has_constituent = Slot(uri=BASE.has_constituent, name="has constituent", curie=BASE.curie('has_constituent'),
                   model_uri=BASE.has_constituent, domain=NamedThing, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.has_administrative_operation = Slot(uri=BASE.has_administrative_operation, name="has administrative operation", curie=BASE.curie('has_administrative_operation'),
                   model_uri=BASE.has_administrative_operation, domain=NamedThing, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]])

slots.has_device = Slot(uri=BASE.has_device, name="has device", curie=BASE.curie('has_device'),
                   model_uri=BASE.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]])

slots.has_procedure = Slot(uri=BASE.has_procedure, name="has procedure", curie=BASE.curie('has_procedure'),
                   model_uri=BASE.has_procedure, domain=NamedThing, range=Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]])

slots.has_receiver = Slot(uri=BASE.has_receiver, name="has receiver", curie=BASE.curie('has_receiver'),
                   model_uri=BASE.has_receiver, domain=None, range=Optional[Union[str, SystemEntityId]])

slots.has_stressor = Slot(uri=BASE.has_stressor, name="has stressor", curie=BASE.curie('has_stressor'),
                   model_uri=BASE.has_stressor, domain=None, range=Optional[str])

slots.has_route = Slot(uri=BASE.has_route, name="has route", curie=BASE.curie('has_route'),
                   model_uri=BASE.has_route, domain=None, range=Optional[str])

slots.population_context_qualifier = Slot(uri=BASE.population_context_qualifier, name="population context qualifier", curie=BASE.curie('population_context_qualifier'),
                   model_uri=BASE.population_context_qualifier, domain=Association, range=Optional[Union[str, PopulationOfIndividualSystemsId]])

slots.temporal_context_qualifier = Slot(uri=BASE.temporal_context_qualifier, name="temporal context qualifier", curie=BASE.curie('temporal_context_qualifier'),
                   model_uri=BASE.temporal_context_qualifier, domain=Association, range=Optional[Union[str, TimeType]])

slots.temporal_interval_qualifier = Slot(uri=BASE.temporal_interval_qualifier, name="temporal interval qualifier", curie=BASE.curie('temporal_interval_qualifier'),
                   model_uri=BASE.temporal_interval_qualifier, domain=Association, range=Optional[Union[str, TimeType]])

slots.is_supplement = Slot(uri=BASE.is_supplement, name="is supplement", curie=BASE.curie('is_supplement'),
                   model_uri=BASE.is_supplement, domain=NamedThing, range=Optional[Union[str, ControlMixtureId]])

slots.trade_name = Slot(uri=BASE.trade_name, name="trade name", curie=BASE.curie('trade_name'),
                   model_uri=BASE.trade_name, domain=NamedThing, range=Optional[Union[str, ControlEntityId]])

slots.available_from = Slot(uri=BASE.available_from, name="available from", curie=BASE.curie('available_from'),
                   model_uri=BASE.available_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_toxic = Slot(uri=BASE.is_toxic, name="is toxic", curie=BASE.curie('is_toxic'),
                   model_uri=BASE.is_toxic, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.has_control_role = Slot(uri=BASE.has_control_role, name="has control role", curie=BASE.curie('has_control_role'),
                   model_uri=BASE.has_control_role, domain=NamedThing, range=Optional[Union[Union[str, ControlRoleId], List[Union[str, ControlRoleId]]]])

slots.regulator_adverse_event_level = Slot(uri=BASE.regulator_adverse_event_level, name="regulator adverse event level", curie=BASE.curie('regulator_adverse_event_level'),
                   model_uri=BASE.regulator_adverse_event_level, domain=Association, range=Optional[Union[str, "RegulatorAdverseEventEnum"]])

slots.highest_regulator_approval_status = Slot(uri=BASE.highest_regulator_approval_status, name="highest regulator approval status", curie=BASE.curie('highest_regulator_approval_status'),
                   model_uri=BASE.highest_regulator_approval_status, domain=None, range=Optional[str])

slots.administrative_operation_regulatory_status_world_wide = Slot(uri=BASE.administrative_operation_regulatory_status_world_wide, name="administrative operation regulatory status world wide", curie=BASE.curie('administrative_operation_regulatory_status_world_wide'),
                   model_uri=BASE.administrative_operation_regulatory_status_world_wide, domain=None, range=Optional[str])

slots.routes_of_delivery = Slot(uri=BASE.routes_of_delivery, name="routes of delivery", curie=BASE.curie('routes_of_delivery'),
                   model_uri=BASE.routes_of_delivery, domain=None, range=Optional[Union[Union[str, "DeliveryEnum"], List[Union[str, "DeliveryEnum"]]]])

slots.aspect_qualifier = Slot(uri=BASE.aspect_qualifier, name="aspect qualifier", curie=BASE.curie('aspect_qualifier'),
                   model_uri=BASE.aspect_qualifier, domain=Association, range=Optional[str])

slots.derivative_qualifier = Slot(uri=BASE.derivative_qualifier, name="derivative qualifier", curie=BASE.curie('derivative_qualifier'),
                   model_uri=BASE.derivative_qualifier, domain=Association, range=Optional[str])

slots.part_qualifier = Slot(uri=BASE.part_qualifier, name="part qualifier", curie=BASE.curie('part_qualifier'),
                   model_uri=BASE.part_qualifier, domain=Association, range=Optional[str])

slots.context_qualifier = Slot(uri=BASE.context_qualifier, name="context qualifier", curie=BASE.curie('context_qualifier'),
                   model_uri=BASE.context_qualifier, domain=Association, range=Optional[str])

slots.direction_qualifier = Slot(uri=BASE.direction_qualifier, name="direction qualifier", curie=BASE.curie('direction_qualifier'),
                   model_uri=BASE.direction_qualifier, domain=Association, range=Optional[str])

slots.exact_matches = Slot(uri=BASE.exact_matches, name="exact matches", curie=BASE.curie('exact_matches'),
                   model_uri=BASE.exact_matches, domain=None, range=Optional[Union[str, List[str]]])

slots.narrow_matches = Slot(uri=BASE.narrow_matches, name="narrow matches", curie=BASE.curie('narrow_matches'),
                   model_uri=BASE.narrow_matches, domain=None, range=Optional[Union[str, List[str]]])

slots.broad_matches = Slot(uri=BASE.broad_matches, name="broad matches", curie=BASE.curie('broad_matches'),
                   model_uri=BASE.broad_matches, domain=None, range=Optional[Union[str, List[str]]])

slots.qualified_predicate = Slot(uri=BASE.qualified_predicate, name="qualified predicate", curie=BASE.curie('qualified_predicate'),
                   model_uri=BASE.qualified_predicate, domain=Association, range=Optional[str])

slots.statement_qualifier = Slot(uri=BASE.statement_qualifier, name="statement qualifier", curie=BASE.curie('statement_qualifier'),
                   model_uri=BASE.statement_qualifier, domain=Association, range=Optional[str])

slots.causal_mechanism_qualifier = Slot(uri=BASE.causal_mechanism_qualifier, name="causal mechanism qualifier", curie=BASE.curie('causal_mechanism_qualifier'),
                   model_uri=BASE.causal_mechanism_qualifier, domain=Association, range=Optional[str])

slots.qualifiers = Slot(uri=BASE.qualifiers, name="qualifiers", curie=BASE.curie('qualifiers'),
                   model_uri=BASE.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=BASE.frequency_qualifier, name="frequency qualifier", curie=BASE.curie('frequency_qualifier'),
                   model_uri=BASE.frequency_qualifier, domain=Association, range=Optional[Union[str, FrequencyValue]])

slots.severity_qualifier = Slot(uri=BASE.severity_qualifier, name="severity qualifier", curie=BASE.curie('severity_qualifier'),
                   model_uri=BASE.severity_qualifier, domain=Association, range=Optional[Union[str, SeverityValueId]])

slots.sex_qualifier = Slot(uri=BASE.sex_qualifier, name="sex qualifier", curie=BASE.curie('sex_qualifier'),
                   model_uri=BASE.sex_qualifier, domain=Association, range=Optional[Union[str, BiologicalSexId]])

slots.onset_qualifier = Slot(uri=BASE.onset_qualifier, name="onset qualifier", curie=BASE.curie('onset_qualifier'),
                   model_uri=BASE.onset_qualifier, domain=Association, range=Optional[Union[str, OnsetId]])

slots.empirical_modifier_qualifier = Slot(uri=BASE.empirical_modifier_qualifier, name="empirical modifier qualifier", curie=BASE.curie('empirical_modifier_qualifier'),
                   model_uri=BASE.empirical_modifier_qualifier, domain=Association, range=Optional[Union[str, EmpiricalModifierId]])

slots.quantifier_qualifier = Slot(uri=BASE.quantifier_qualifier, name="quantifier qualifier", curie=BASE.curie('quantifier_qualifier'),
                   model_uri=BASE.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.catalyst_qualifier = Slot(uri=BASE.catalyst_qualifier, name="catalyst qualifier", curie=BASE.curie('catalyst_qualifier'),
                   model_uri=BASE.catalyst_qualifier, domain=Association, range=Optional[Union[Union[dict, AssemblyMixin], List[Union[dict, AssemblyMixin]]]])

slots.stage_qualifier = Slot(uri=BASE.stage_qualifier, name="stage qualifier", curie=BASE.curie('stage_qualifier'),
                   model_uri=BASE.stage_qualifier, domain=Association, range=Optional[Union[str, LifecycleStageId]])

slots.related_to = Slot(uri=BASE.related_to, name="related to", curie=BASE.curie('related_to'),
                   model_uri=BASE.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_to_at_concept_level = Slot(uri=BASE.related_to_at_concept_level, name="related to at concept level", curie=BASE.curie('related_to_at_concept_level'),
                   model_uri=BASE.related_to_at_concept_level, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_to_at_instance_level = Slot(uri=BASE.related_to_at_instance_level, name="related to at instance level", curie=BASE.curie('related_to_at_instance_level'),
                   model_uri=BASE.related_to_at_instance_level, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with = Slot(uri=BASE.associated_with, name="associated with", curie=BASE.curie('associated_with'),
                   model_uri=BASE.associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.superclass_of = Slot(uri=BASE.superclass_of, name="superclass of", curie=BASE.curie('superclass_of'),
                   model_uri=BASE.superclass_of, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.subclass_of = Slot(uri=BASE.subclass_of, name="subclass of", curie=BASE.curie('subclass_of'),
                   model_uri=BASE.subclass_of, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.same_as = Slot(uri=BASE.same_as, name="same as", curie=BASE.curie('same_as'),
                   model_uri=BASE.same_as, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.close_match = Slot(uri=BASE.close_match, name="close match", curie=BASE.curie('close_match'),
                   model_uri=BASE.close_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.exact_match = Slot(uri=BASE.exact_match, name="exact match", curie=BASE.curie('exact_match'),
                   model_uri=BASE.exact_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.broad_match = Slot(uri=BASE.broad_match, name="broad match", curie=BASE.curie('broad_match'),
                   model_uri=BASE.broad_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.narrow_match = Slot(uri=BASE.narrow_match, name="narrow match", curie=BASE.curie('narrow_match'),
                   model_uri=BASE.narrow_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.member_of = Slot(uri=BASE.member_of, name="member of", curie=BASE.curie('member_of'),
                   model_uri=BASE.member_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_member = Slot(uri=BASE.has_member, name="has member", curie=BASE.curie('has_member'),
                   model_uri=BASE.has_member, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.opposite_of = Slot(uri=BASE.opposite_of, name="opposite of", curie=BASE.curie('opposite_of'),
                   model_uri=BASE.opposite_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with_likelihood_of = Slot(uri=BASE.associated_with_likelihood_of, name="associated with likelihood of", curie=BASE.curie('associated_with_likelihood_of'),
                   model_uri=BASE.associated_with_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.likelihood_associated_with = Slot(uri=BASE.likelihood_associated_with, name="likelihood associated with", curie=BASE.curie('likelihood_associated_with'),
                   model_uri=BASE.likelihood_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with_increased_likelihood_of = Slot(uri=BASE.associated_with_increased_likelihood_of, name="associated with increased likelihood of", curie=BASE.curie('associated_with_increased_likelihood_of'),
                   model_uri=BASE.associated_with_increased_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.increased_likelihood_associated_with = Slot(uri=BASE.increased_likelihood_associated_with, name="increased likelihood associated with", curie=BASE.curie('increased_likelihood_associated_with'),
                   model_uri=BASE.increased_likelihood_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with_decreased_likelihood_of = Slot(uri=BASE.associated_with_decreased_likelihood_of, name="associated with decreased likelihood of", curie=BASE.curie('associated_with_decreased_likelihood_of'),
                   model_uri=BASE.associated_with_decreased_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreased_likelihood_associated_with = Slot(uri=BASE.decreased_likelihood_associated_with, name="decreased likelihood associated with", curie=BASE.curie('decreased_likelihood_associated_with'),
                   model_uri=BASE.decreased_likelihood_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.target_for = Slot(uri=BASE.target_for, name="target for", curie=BASE.curie('target_for'),
                   model_uri=BASE.target_for, domain=Class, range=Optional[Union[Union[str, FaultId], List[Union[str, FaultId]]]])

slots.has_target = Slot(uri=BASE.has_target, name="has target", curie=BASE.curie('has_target'),
                   model_uri=BASE.has_target, domain=Fault, range=Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]])

slots.active_in = Slot(uri=BASE.active_in, name="active in", curie=BASE.curie('active_in'),
                   model_uri=BASE.active_in, domain=None, range=Optional[Union[Union[str, ComponentId], List[Union[str, ComponentId]]]])

slots.has_active_component = Slot(uri=BASE.has_active_component, name="has active component", curie=BASE.curie('has_active_component'),
                   model_uri=BASE.has_active_component, domain=Component, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.acts_upstream_of = Slot(uri=BASE.acts_upstream_of, name="acts upstream of", curie=BASE.curie('acts_upstream_of'),
                   model_uri=BASE.acts_upstream_of, domain=None, range=Optional[Union[Union[str, ComputationalProcessId], List[Union[str, ComputationalProcessId]]]])

slots.has_upstream_actor = Slot(uri=BASE.has_upstream_actor, name="has upstream actor", curie=BASE.curie('has_upstream_actor'),
                   model_uri=BASE.has_upstream_actor, domain=ComputationalProcess, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.acts_upstream_of_positive_effect = Slot(uri=BASE.acts_upstream_of_positive_effect, name="acts upstream of positive effect", curie=BASE.curie('acts_upstream_of_positive_effect'),
                   model_uri=BASE.acts_upstream_of_positive_effect, domain=None, range=Optional[Union[Union[str, ComputationalProcessId], List[Union[str, ComputationalProcessId]]]])

slots.has_positive_upstream_actor = Slot(uri=BASE.has_positive_upstream_actor, name="has positive upstream actor", curie=BASE.curie('has_positive_upstream_actor'),
                   model_uri=BASE.has_positive_upstream_actor, domain=ComputationalProcess, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.acts_upstream_of_negative_effect = Slot(uri=BASE.acts_upstream_of_negative_effect, name="acts upstream of negative effect", curie=BASE.curie('acts_upstream_of_negative_effect'),
                   model_uri=BASE.acts_upstream_of_negative_effect, domain=None, range=Optional[Union[Union[str, ComputationalProcessId], List[Union[str, ComputationalProcessId]]]])

slots.has_negative_upstream_actor = Slot(uri=BASE.has_negative_upstream_actor, name="has negative upstream actor", curie=BASE.curie('has_negative_upstream_actor'),
                   model_uri=BASE.has_negative_upstream_actor, domain=ComputationalProcess, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.acts_upstream_of_or_within = Slot(uri=BASE.acts_upstream_of_or_within, name="acts upstream of or within", curie=BASE.curie('acts_upstream_of_or_within'),
                   model_uri=BASE.acts_upstream_of_or_within, domain=None, range=Optional[Union[Union[str, ComputationalProcessId], List[Union[str, ComputationalProcessId]]]])

slots.has_upstream_or_within_actor = Slot(uri=BASE.has_upstream_or_within_actor, name="has upstream or within actor", curie=BASE.curie('has_upstream_or_within_actor'),
                   model_uri=BASE.has_upstream_or_within_actor, domain=ComputationalProcess, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.acts_upstream_of_or_within_positive_effect = Slot(uri=BASE.acts_upstream_of_or_within_positive_effect, name="acts upstream of or within positive effect", curie=BASE.curie('acts_upstream_of_or_within_positive_effect'),
                   model_uri=BASE.acts_upstream_of_or_within_positive_effect, domain=None, range=Optional[Union[Union[str, ComputationalProcessId], List[Union[str, ComputationalProcessId]]]])

slots.has_positive_upstream_or_within_actor = Slot(uri=BASE.has_positive_upstream_or_within_actor, name="has positive upstream or within actor", curie=BASE.curie('has_positive_upstream_or_within_actor'),
                   model_uri=BASE.has_positive_upstream_or_within_actor, domain=ComputationalProcess, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.acts_upstream_of_or_within_negative_effect = Slot(uri=BASE.acts_upstream_of_or_within_negative_effect, name="acts upstream of or within negative effect", curie=BASE.curie('acts_upstream_of_or_within_negative_effect'),
                   model_uri=BASE.acts_upstream_of_or_within_negative_effect, domain=None, range=Optional[Union[Union[str, ComputationalProcessId], List[Union[str, ComputationalProcessId]]]])

slots.has_negative_upstream_or_within_actor = Slot(uri=BASE.has_negative_upstream_or_within_actor, name="has negative upstream or within actor", curie=BASE.curie('has_negative_upstream_or_within_actor'),
                   model_uri=BASE.has_negative_upstream_or_within_actor, domain=ComputationalProcess, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.mentions = Slot(uri=BASE.mentions, name="mentions", curie=BASE.curie('mentions'),
                   model_uri=BASE.mentions, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.mentioned_by = Slot(uri=BASE.mentioned_by, name="mentioned by", curie=BASE.curie('mentioned_by'),
                   model_uri=BASE.mentioned_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=BASE.contributor, name="contributor", curie=BASE.curie('contributor'),
                   model_uri=BASE.contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_contributor = Slot(uri=BASE.has_contributor, name="has contributor", curie=BASE.curie('has_contributor'),
                   model_uri=BASE.has_contributor, domain=Agent, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.provider = Slot(uri=BASE.provider, name="provider", curie=BASE.curie('provider'),
                   model_uri=BASE.provider, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_provider = Slot(uri=BASE.has_provider, name="has provider", curie=BASE.curie('has_provider'),
                   model_uri=BASE.has_provider, domain=Agent, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.publisher = Slot(uri=BASE.publisher, name="publisher", curie=BASE.curie('publisher'),
                   model_uri=BASE.publisher, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_publisher = Slot(uri=BASE.has_publisher, name="has publisher", curie=BASE.curie('has_publisher'),
                   model_uri=BASE.has_publisher, domain=Agent, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.editor = Slot(uri=BASE.editor, name="editor", curie=BASE.curie('editor'),
                   model_uri=BASE.editor, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_editor = Slot(uri=BASE.has_editor, name="has editor", curie=BASE.curie('has_editor'),
                   model_uri=BASE.has_editor, domain=Agent, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.author = Slot(uri=BASE.author, name="author", curie=BASE.curie('author'),
                   model_uri=BASE.author, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_author = Slot(uri=BASE.has_author, name="has author", curie=BASE.curie('has_author'),
                   model_uri=BASE.has_author, domain=Agent, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.assesses = Slot(uri=BASE.assesses, name="assesses", curie=BASE.curie('assesses'),
                   model_uri=BASE.assesses, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_assessed_by = Slot(uri=BASE.is_assessed_by, name="is assessed by", curie=BASE.curie('is_assessed_by'),
                   model_uri=BASE.is_assessed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.interacts_with = Slot(uri=BASE.interacts_with, name="interacts with", curie=BASE.curie('interacts_with'),
                   model_uri=BASE.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.physically_interacts_with = Slot(uri=BASE.physically_interacts_with, name="physically interacts with", curie=BASE.curie('physically_interacts_with'),
                   model_uri=BASE.physically_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.directly_interacts_with = Slot(uri=BASE.directly_interacts_with, name="directly interacts with", curie=BASE.curie('directly_interacts_with'),
                   model_uri=BASE.directly_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.binds = Slot(uri=BASE.binds, name="binds", curie=BASE.curie('binds'),
                   model_uri=BASE.binds, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.indirectly_interacts_with = Slot(uri=BASE.indirectly_interacts_with, name="indirectly interacts with", curie=BASE.curie('indirectly_interacts_with'),
                   model_uri=BASE.indirectly_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affects = Slot(uri=BASE.affects, name="affects", curie=BASE.curie('affects'),
                   model_uri=BASE.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=BASE.affected_by, name="affected by", curie=BASE.curie('affected_by'),
                   model_uri=BASE.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with_sensitivity_to = Slot(uri=BASE.associated_with_sensitivity_to, name="associated with sensitivity to", curie=BASE.curie('associated_with_sensitivity_to'),
                   model_uri=BASE.associated_with_sensitivity_to, domain=NamedThing, range=Optional[Union[Union[str, ControlEntityId], List[Union[str, ControlEntityId]]]])

slots.sensitivity_associated_with = Slot(uri=BASE.sensitivity_associated_with, name="sensitivity associated with", curie=BASE.curie('sensitivity_associated_with'),
                   model_uri=BASE.sensitivity_associated_with, domain=ControlEntity, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with_resistance_to = Slot(uri=BASE.associated_with_resistance_to, name="associated with resistance to", curie=BASE.curie('associated_with_resistance_to'),
                   model_uri=BASE.associated_with_resistance_to, domain=NamedThing, range=Optional[Union[Union[str, ControlEntityId], List[Union[str, ControlEntityId]]]])

slots.resistance_associated_with = Slot(uri=BASE.resistance_associated_with, name="resistance associated with", curie=BASE.curie('resistance_associated_with'),
                   model_uri=BASE.resistance_associated_with, domain=ControlEntity, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.diagnoses = Slot(uri=BASE.diagnoses, name="diagnoses", curie=BASE.curie('diagnoses'),
                   model_uri=BASE.diagnoses, domain=None, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.is_diagnosed_by = Slot(uri=BASE.is_diagnosed_by, name="is diagnosed by", curie=BASE.curie('is_diagnosed_by'),
                   model_uri=BASE.is_diagnosed_by, domain=FaultOrObservableFeature, range=Optional[Union[Union[dict, ControlOrAdministrativeOperationOrRestoration], List[Union[dict, ControlOrAdministrativeOperationOrRestoration]]]])

slots.increases_amount_or_activity_of = Slot(uri=BASE.increases_amount_or_activity_of, name="increases amount or activity of", curie=BASE.curie('increases_amount_or_activity_of'),
                   model_uri=BASE.increases_amount_or_activity_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.amount_or_activity_increased_by = Slot(uri=BASE.amount_or_activity_increased_by, name="amount or activity increased by", curie=BASE.curie('amount_or_activity_increased_by'),
                   model_uri=BASE.amount_or_activity_increased_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreases_amount_or_activity_of = Slot(uri=BASE.decreases_amount_or_activity_of, name="decreases amount or activity of", curie=BASE.curie('decreases_amount_or_activity_of'),
                   model_uri=BASE.decreases_amount_or_activity_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.amount_or_activity_decreased_by = Slot(uri=BASE.amount_or_activity_decreased_by, name="amount or activity decreased by", curie=BASE.curie('amount_or_activity_decreased_by'),
                   model_uri=BASE.amount_or_activity_decreased_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.control_role_mixin = Slot(uri=BASE.control_role_mixin, name="control role mixin", curie=BASE.curie('control_role_mixin'),
                   model_uri=BASE.control_role_mixin, domain=None, range=Optional[str])

slots.computational_role_mixin = Slot(uri=BASE.computational_role_mixin, name="computational role mixin", curie=BASE.curie('computational_role_mixin'),
                   model_uri=BASE.computational_role_mixin, domain=None, range=Optional[str])

slots.affects_response_to = Slot(uri=BASE.affects_response_to, name="affects response to", curie=BASE.curie('affects_response_to'),
                   model_uri=BASE.affects_response_to, domain=None, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.response_affected_by = Slot(uri=BASE.response_affected_by, name="response affected by", curie=BASE.curie('response_affected_by'),
                   model_uri=BASE.response_affected_by, domain=None, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.increases_response_to = Slot(uri=BASE.increases_response_to, name="increases response to", curie=BASE.curie('increases_response_to'),
                   model_uri=BASE.increases_response_to, domain=None, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.response_increased_by = Slot(uri=BASE.response_increased_by, name="response increased by", curie=BASE.curie('response_increased_by'),
                   model_uri=BASE.response_increased_by, domain=None, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.decreases_response_to = Slot(uri=BASE.decreases_response_to, name="decreases response to", curie=BASE.curie('decreases_response_to'),
                   model_uri=BASE.decreases_response_to, domain=None, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.response_decreased_by = Slot(uri=BASE.response_decreased_by, name="response decreased by", curie=BASE.curie('response_decreased_by'),
                   model_uri=BASE.response_decreased_by, domain=None, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.regulates = Slot(uri=BASE.regulates, name="regulates", curie=BASE.curie('regulates'),
                   model_uri=BASE.regulates, domain=None, range=Optional[Union[Union[dict, "TangibleEssenceOrOccurrent"], List[Union[dict, "TangibleEssenceOrOccurrent"]]]])

slots.regulated_by = Slot(uri=BASE.regulated_by, name="regulated by", curie=BASE.curie('regulated_by'),
                   model_uri=BASE.regulated_by, domain=None, range=Optional[Union[Union[dict, "TangibleEssenceOrOccurrent"], List[Union[dict, "TangibleEssenceOrOccurrent"]]]])

slots.disrupts = Slot(uri=BASE.disrupts, name="disrupts", curie=BASE.curie('disrupts'),
                   model_uri=BASE.disrupts, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.disrupted_by = Slot(uri=BASE.disrupted_by, name="disrupted by", curie=BASE.curie('disrupted_by'),
                   model_uri=BASE.disrupted_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.subclasses_of = Slot(uri=BASE.subclasses_of, name="subclasses of", curie=BASE.curie('subclasses_of'),
                   model_uri=BASE.subclasses_of, domain=None, range=Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]])

slots.has_subclasses = Slot(uri=BASE.has_subclasses, name="has subclasses", curie=BASE.curie('has_subclasses'),
                   model_uri=BASE.has_subclasses, domain=Class, range=Optional[Union[Union[dict, "SubclassesMixin"], List[Union[dict, "SubclassesMixin"]]]])

slots.replicated_to = Slot(uri=BASE.replicated_to, name="replicated to", curie=BASE.curie('replicated_to'),
                   model_uri=BASE.replicated_to, domain=Class, range=Optional[Union[Union[str, ReplicaId], List[Union[str, ReplicaId]]]])

slots.replicated_from = Slot(uri=BASE.replicated_from, name="replicated from", curie=BASE.curie('replicated_from'),
                   model_uri=BASE.replicated_from, domain=Replica, range=Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]])

slots.translates_to = Slot(uri=BASE.translates_to, name="translates to", curie=BASE.curie('translates_to'),
                   model_uri=BASE.translates_to, domain=Replica, range=Optional[Union[Union[str, SystemOperationId], List[Union[str, SystemOperationId]]]])

slots.translation_of = Slot(uri=BASE.translation_of, name="translation of", curie=BASE.curie('translation_of'),
                   model_uri=BASE.translation_of, domain=SystemOperation, range=Optional[Union[Union[str, ReplicaId], List[Union[str, ReplicaId]]]])

slots.homologous_to = Slot(uri=BASE.homologous_to, name="homologous to", curie=BASE.curie('homologous_to'),
                   model_uri=BASE.homologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.paralogous_to = Slot(uri=BASE.paralogous_to, name="paralogous to", curie=BASE.curie('paralogous_to'),
                   model_uri=BASE.paralogous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coexists_with = Slot(uri=BASE.coexists_with, name="coexists with", curie=BASE.curie('coexists_with'),
                   model_uri=BASE.coexists_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_pathway_with = Slot(uri=BASE.in_pathway_with, name="in pathway with", curie=BASE.curie('in_pathway_with'),
                   model_uri=BASE.in_pathway_with, domain=None, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.in_component_population_with = Slot(uri=BASE.in_component_population_with, name="in component population with", curie=BASE.curie('in_component_population_with'),
                   model_uri=BASE.in_component_population_with, domain=None, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.colocalizes_with = Slot(uri=BASE.colocalizes_with, name="colocalizes with", curie=BASE.curie('colocalizes_with'),
                   model_uri=BASE.colocalizes_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.inheritance_association = Slot(uri=BASE.inheritance_association, name="inheritance association", curie=BASE.curie('inheritance_association'),
                   model_uri=BASE.inheritance_association, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.class_associated_with_condition = Slot(uri=BASE.class_associated_with_condition, name="class associated with condition", curie=BASE.curie('class_associated_with_condition'),
                   model_uri=BASE.class_associated_with_condition, domain=Class, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.condition_associated_with_class = Slot(uri=BASE.condition_associated_with_class, name="condition associated with class", curie=BASE.curie('condition_associated_with_class'),
                   model_uri=BASE.condition_associated_with_class, domain=FaultOrObservableFeature, range=Optional[Union[Union[str, ClassId], List[Union[str, ClassId]]]])

slots.affects_risk_for = Slot(uri=BASE.affects_risk_for, name="affects risk for", curie=BASE.curie('affects_risk_for'),
                   model_uri=BASE.affects_risk_for, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.risk_affected_by = Slot(uri=BASE.risk_affected_by, name="risk affected by", curie=BASE.curie('risk_affected_by'),
                   model_uri=BASE.risk_affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.predisposes = Slot(uri=BASE.predisposes, name="predisposes", curie=BASE.curie('predisposes'),
                   model_uri=BASE.predisposes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_predisposing_factor = Slot(uri=BASE.has_predisposing_factor, name="has predisposing factor", curie=BASE.curie('has_predisposing_factor'),
                   model_uri=BASE.has_predisposing_factor, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributes_to = Slot(uri=BASE.contributes_to, name="contributes to", curie=BASE.curie('contributes_to'),
                   model_uri=BASE.contributes_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contribution_from = Slot(uri=BASE.contribution_from, name="contribution from", curie=BASE.curie('contribution_from'),
                   model_uri=BASE.contribution_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes = Slot(uri=BASE.causes, name="causes", curie=BASE.curie('causes'),
                   model_uri=BASE.causes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.caused_by = Slot(uri=BASE.caused_by, name="caused by", curie=BASE.curie('caused_by'),
                   model_uri=BASE.caused_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.ameliorates = Slot(uri=BASE.ameliorates, name="ameliorates", curie=BASE.curie('ameliorates'),
                   model_uri=BASE.ameliorates, domain=ComputationalEntity, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.is_ameliorated_by = Slot(uri=BASE.is_ameliorated_by, name="is ameliorated by", curie=BASE.curie('is_ameliorated_by'),
                   model_uri=BASE.is_ameliorated_by, domain=FaultOrObservableFeature, range=Optional[Union[Union[str, ComputationalEntityId], List[Union[str, ComputationalEntityId]]]])

slots.exacerbates = Slot(uri=BASE.exacerbates, name="exacerbates", curie=BASE.curie('exacerbates'),
                   model_uri=BASE.exacerbates, domain=ComputationalEntity, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.is_exacerbated_by = Slot(uri=BASE.is_exacerbated_by, name="is exacerbated by", curie=BASE.curie('is_exacerbated_by'),
                   model_uri=BASE.is_exacerbated_by, domain=FaultOrObservableFeature, range=Optional[Union[Union[str, ComputationalEntityId], List[Union[str, ComputationalEntityId]]]])

slots.treats = Slot(uri=BASE.treats, name="treats", curie=BASE.curie('treats'),
                   model_uri=BASE.treats, domain=None, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.treated_by = Slot(uri=BASE.treated_by, name="treated by", curie=BASE.curie('treated_by'),
                   model_uri=BASE.treated_by, domain=FaultOrObservableFeature, range=Optional[Union[Union[dict, ControlOrAdministrativeOperationOrRestoration], List[Union[dict, ControlOrAdministrativeOperationOrRestoration]]]])

slots.prevents = Slot(uri=BASE.prevents, name="prevents", curie=BASE.curie('prevents'),
                   model_uri=BASE.prevents, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.prevented_by = Slot(uri=BASE.prevented_by, name="prevented by", curie=BASE.curie('prevented_by'),
                   model_uri=BASE.prevented_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.correlated_with = Slot(uri=BASE.correlated_with, name="correlated with", curie=BASE.curie('correlated_with'),
                   model_uri=BASE.correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.positively_correlated_with = Slot(uri=BASE.positively_correlated_with, name="positively correlated with", curie=BASE.curie('positively_correlated_with'),
                   model_uri=BASE.positively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.negatively_correlated_with = Slot(uri=BASE.negatively_correlated_with, name="negatively correlated with", curie=BASE.curie('negatively_correlated_with'),
                   model_uri=BASE.negatively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.occurs_together_in_literature_with = Slot(uri=BASE.occurs_together_in_literature_with, name="occurs together in literature with", curie=BASE.curie('occurs_together_in_literature_with'),
                   model_uri=BASE.occurs_together_in_literature_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coexpressed_with = Slot(uri=BASE.coexpressed_with, name="coexpressed with", curie=BASE.curie('coexpressed_with'),
                   model_uri=BASE.coexpressed_with, domain=None, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.has_marker = Slot(uri=BASE.has_marker, name="has marker", curie=BASE.curie('has_marker'),
                   model_uri=BASE.has_marker, domain=FaultOrObservableFeature, range=Optional[Union[Union[dict, "ControlEntityOrClassOrSubclasses"], List[Union[dict, "ControlEntityOrClassOrSubclasses"]]]])

slots.marker_for = Slot(uri=BASE.marker_for, name="marker for", curie=BASE.curie('marker_for'),
                   model_uri=BASE.marker_for, domain=None, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.expressed_in = Slot(uri=BASE.expressed_in, name="expressed in", curie=BASE.curie('expressed_in'),
                   model_uri=BASE.expressed_in, domain=None, range=Optional[Union[Union[str, DeploymentEntityId], List[Union[str, DeploymentEntityId]]]])

slots.expresses = Slot(uri=BASE.expresses, name="expresses", curie=BASE.curie('expresses'),
                   model_uri=BASE.expresses, domain=DeploymentEntity, range=Optional[Union[Union[dict, "ClassOrSubclasses"], List[Union[dict, "ClassOrSubclasses"]]]])

slots.has_observation = Slot(uri=BASE.has_observation, name="has observation", curie=BASE.curie('has_observation'),
                   model_uri=BASE.has_observation, domain=ComputationalEntity, range=Optional[Union[Union[str, ObservableFeatureId], List[Union[str, ObservableFeatureId]]]])

slots.observation_of = Slot(uri=BASE.observation_of, name="observation of", curie=BASE.curie('observation_of'),
                   model_uri=BASE.observation_of, domain=ObservableFeature, range=Optional[Union[Union[str, ComputationalEntityId], List[Union[str, ComputationalEntityId]]]])

slots.occurs_in = Slot(uri=BASE.occurs_in, name="occurs in", curie=BASE.curie('occurs_in'),
                   model_uri=BASE.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contains_process = Slot(uri=BASE.contains_process, name="contains process", curie=BASE.curie('contains_process'),
                   model_uri=BASE.contains_process, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=BASE.located_in, name="located in", curie=BASE.curie('located_in'),
                   model_uri=BASE.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=BASE.location_of, name="location of", curie=BASE.curie('location_of'),
                   model_uri=BASE.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.fault_has_location = Slot(uri=BASE.fault_has_location, name="fault has location", curie=BASE.curie('fault_has_location'),
                   model_uri=BASE.fault_has_location, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of_fault = Slot(uri=BASE.location_of_fault, name="location of fault", curie=BASE.curie('location_of_fault'),
                   model_uri=BASE.location_of_fault, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=BASE.similar_to, name="similar to", curie=BASE.curie('similar_to'),
                   model_uri=BASE.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_sequence_location = Slot(uri=BASE.has_sequence_location, name="has sequence location", curie=BASE.curie('has_sequence_location'),
                   model_uri=BASE.has_sequence_location, domain=None, range=Optional[Union[Union[dict, "WorkloadEntity"], List[Union[dict, "WorkloadEntity"]]]])

slots.sequence_location_of = Slot(uri=BASE.sequence_location_of, name="sequence location of", curie=BASE.curie('sequence_location_of'),
                   model_uri=BASE.sequence_location_of, domain=None, range=Optional[Union[Union[dict, "WorkloadEntity"], List[Union[dict, "WorkloadEntity"]]]])

slots.model_of = Slot(uri=BASE.model_of, name="model of", curie=BASE.curie('model_of'),
                   model_uri=BASE.model_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.models = Slot(uri=BASE.models, name="models", curie=BASE.curie('models'),
                   model_uri=BASE.models, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.overlaps = Slot(uri=BASE.overlaps, name="overlaps", curie=BASE.curie('overlaps'),
                   model_uri=BASE.overlaps, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_part = Slot(uri=BASE.has_part, name="has part", curie=BASE.curie('has_part'),
                   model_uri=BASE.has_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.composed_primarily_of = Slot(uri=BASE.composed_primarily_of, name="composed primarily of", curie=BASE.curie('composed_primarily_of'),
                   model_uri=BASE.composed_primarily_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.primarily_composed_of = Slot(uri=BASE.primarily_composed_of, name="primarily composed of", curie=BASE.curie('primarily_composed_of'),
                   model_uri=BASE.primarily_composed_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=BASE.part_of, name="part of", curie=BASE.curie('part_of'),
                   model_uri=BASE.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_input = Slot(uri=BASE.has_input, name="has input", curie=BASE.curie('has_input'),
                   model_uri=BASE.has_input, domain=None, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.is_input_of = Slot(uri=BASE.is_input_of, name="is input of", curie=BASE.curie('is_input_of'),
                   model_uri=BASE.is_input_of, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[dict, Occurrent], List[Union[dict, Occurrent]]]])

slots.has_output = Slot(uri=BASE.has_output, name="has output", curie=BASE.curie('has_output'),
                   model_uri=BASE.has_output, domain=None, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.is_output_of = Slot(uri=BASE.is_output_of, name="is output of", curie=BASE.curie('is_output_of'),
                   model_uri=BASE.is_output_of, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[dict, Occurrent], List[Union[dict, Occurrent]]]])

slots.has_participant = Slot(uri=BASE.has_participant, name="has participant", curie=BASE.curie('has_participant'),
                   model_uri=BASE.has_participant, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.catalyzes = Slot(uri=BASE.catalyzes, name="catalyzes", curie=BASE.curie('catalyzes'),
                   model_uri=BASE.catalyzes, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.has_catalyst = Slot(uri=BASE.has_catalyst, name="has catalyst", curie=BASE.curie('has_catalyst'),
                   model_uri=BASE.has_catalyst, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_platform = Slot(uri=BASE.has_platform, name="has platform", curie=BASE.curie('has_platform'),
                   model_uri=BASE.has_platform, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_platform_of = Slot(uri=BASE.is_platform_of, name="is platform of", curie=BASE.curie('is_platform_of'),
                   model_uri=BASE.is_platform_of, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.participates_in = Slot(uri=BASE.participates_in, name="participates in", curie=BASE.curie('participates_in'),
                   model_uri=BASE.participates_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.actively_involved_in = Slot(uri=BASE.actively_involved_in, name="actively involved in", curie=BASE.curie('actively_involved_in'),
                   model_uri=BASE.actively_involved_in, domain=OperationalActivity, range=Optional[Union[Union[dict, Occurrent], List[Union[dict, Occurrent]]]])

slots.actively_involves = Slot(uri=BASE.actively_involves, name="actively involves", curie=BASE.curie('actively_involves'),
                   model_uri=BASE.actively_involves, domain=None, range=Optional[Union[Union[str, OperationalActivityId], List[Union[str, OperationalActivityId]]]])

slots.capable_of = Slot(uri=BASE.capable_of, name="capable of", curie=BASE.curie('capable_of'),
                   model_uri=BASE.capable_of, domain=OperationalActivity, range=Optional[Union[Union[dict, Occurrent], List[Union[dict, Occurrent]]]])

slots.has_capability = Slot(uri=BASE.has_capability, name="has capability", curie=BASE.curie('has_capability'),
                   model_uri=BASE.has_capability, domain=None, range=Optional[Union[Union[str, OperationalActivityId], List[Union[str, OperationalActivityId]]]])

slots.enables = Slot(uri=BASE.enables, name="enables", curie=BASE.curie('enables'),
                   model_uri=BASE.enables, domain=SystemEntity, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=BASE.enabled_by, name="enabled by", curie=BASE.curie('enabled_by'),
                   model_uri=BASE.enabled_by, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[str, SystemEntityId], List[Union[str, SystemEntityId]]]])

slots.derives_into = Slot(uri=BASE.derives_into, name="derives into", curie=BASE.curie('derives_into'),
                   model_uri=BASE.derives_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.derives_from = Slot(uri=BASE.derives_from, name="derives from", curie=BASE.curie('derives_from'),
                   model_uri=BASE.derives_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_controller_of = Slot(uri=BASE.is_controller_of, name="is controller of", curie=BASE.curie('is_controller_of'),
                   model_uri=BASE.is_controller_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.has_controller = Slot(uri=BASE.has_controller, name="has controller", curie=BASE.curie('has_controller'),
                   model_uri=BASE.has_controller, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.is_active_ingredient_of = Slot(uri=BASE.is_active_ingredient_of, name="is active ingredient of", curie=BASE.curie('is_active_ingredient_of'),
                   model_uri=BASE.is_active_ingredient_of, domain=OperationalEntity, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [RO["0002249"]])

slots.has_active_ingredient = Slot(uri=BASE.has_active_ingredient, name="has active ingredient", curie=BASE.curie('has_active_ingredient'),
                   model_uri=BASE.has_active_ingredient, domain=AdministrativeOperation, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]], mappings = [RO["0002248"]])

slots.is_excipient_of = Slot(uri=BASE.is_excipient_of, name="is excipient of", curie=BASE.curie('is_excipient_of'),
                   model_uri=BASE.is_excipient_of, domain=OperationalEntity, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [WIKIDATA.Q902638])

slots.has_excipient = Slot(uri=BASE.has_excipient, name="has excipient", curie=BASE.curie('has_excipient'),
                   model_uri=BASE.has_excipient, domain=AdministrativeOperation, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]], mappings = [WIKIDATA.Q902638])

slots.manifestation_of = Slot(uri=BASE.manifestation_of, name="manifestation of", curie=BASE.curie('manifestation_of'),
                   model_uri=BASE.manifestation_of, domain=NamedThing, range=Optional[Union[Union[str, FaultId], List[Union[str, FaultId]]]])

slots.has_manifestation = Slot(uri=BASE.has_manifestation, name="has manifestation", curie=BASE.curie('has_manifestation'),
                   model_uri=BASE.has_manifestation, domain=Fault, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.mode_of_inheritance_of = Slot(uri=BASE.mode_of_inheritance_of, name="mode of inheritance of", curie=BASE.curie('mode_of_inheritance_of'),
                   model_uri=BASE.mode_of_inheritance_of, domain=Inheritance, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.has_mode_of_inheritance = Slot(uri=BASE.has_mode_of_inheritance, name="has mode of inheritance", curie=BASE.curie('has_mode_of_inheritance'),
                   model_uri=BASE.has_mode_of_inheritance, domain=FaultOrObservableFeature, range=Optional[Union[Union[str, InheritanceId], List[Union[str, InheritanceId]]]])

slots.produces = Slot(uri=BASE.produces, name="produces", curie=BASE.curie('produces'),
                   model_uri=BASE.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=BASE.produced_by, name="produced by", curie=BASE.curie('produced_by'),
                   model_uri=BASE.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.consumes = Slot(uri=BASE.consumes, name="consumes", curie=BASE.curie('consumes'),
                   model_uri=BASE.consumes, domain=None, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.consumed_by = Slot(uri=BASE.consumed_by, name="consumed by", curie=BASE.curie('consumed_by'),
                   model_uri=BASE.consumed_by, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[dict, Occurrent], List[Union[dict, Occurrent]]]])

slots.temporally_related_to = Slot(uri=BASE.temporally_related_to, name="temporally related to", curie=BASE.curie('temporally_related_to'),
                   model_uri=BASE.temporally_related_to, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.precedes = Slot(uri=BASE.precedes, name="precedes", curie=BASE.curie('precedes'),
                   model_uri=BASE.precedes, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.preceded_by = Slot(uri=BASE.preceded_by, name="preceded by", curie=BASE.curie('preceded_by'),
                   model_uri=BASE.preceded_by, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.has_variant_part = Slot(uri=BASE.has_variant_part, name="has variant part", curie=BASE.curie('has_variant_part'),
                   model_uri=BASE.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.variant_part_of = Slot(uri=BASE.variant_part_of, name="variant part of", curie=BASE.curie('variant_part_of'),
                   model_uri=BASE.variant_part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=BASE.related_condition, name="related condition", curie=BASE.curie('related_condition'),
                   model_uri=BASE.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.fault_has_basis_in = Slot(uri=BASE.fault_has_basis_in, name="fault has basis in", curie=BASE.curie('fault_has_basis_in'),
                   model_uri=BASE.fault_has_basis_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.occurs_in_fault = Slot(uri=BASE.occurs_in_fault, name="occurs in fault", curie=BASE.curie('occurs_in_fault'),
                   model_uri=BASE.occurs_in_fault, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_adverse_event = Slot(uri=BASE.has_adverse_event, name="has adverse event", curie=BASE.curie('has_adverse_event'),
                   model_uri=BASE.has_adverse_event, domain=None, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.adverse_event_of = Slot(uri=BASE.adverse_event_of, name="adverse event of", curie=BASE.curie('adverse_event_of'),
                   model_uri=BASE.adverse_event_of, domain=FaultOrObservableFeature, range=Optional[Union[Union[dict, ControlOrAdministrativeOperationOrRestoration], List[Union[dict, ControlOrAdministrativeOperationOrRestoration]]]])

slots.has_side_effect = Slot(uri=BASE.has_side_effect, name="has side effect", curie=BASE.curie('has_side_effect'),
                   model_uri=BASE.has_side_effect, domain=None, range=Optional[Union[Union[str, FaultOrObservableFeatureId], List[Union[str, FaultOrObservableFeatureId]]]])

slots.is_side_effect_of = Slot(uri=BASE.is_side_effect_of, name="is side effect of", curie=BASE.curie('is_side_effect_of'),
                   model_uri=BASE.is_side_effect_of, domain=FaultOrObservableFeature, range=Optional[Union[Union[dict, ControlOrAdministrativeOperationOrRestoration], List[Union[dict, ControlOrAdministrativeOperationOrRestoration]]]])

slots.has_not_completed = Slot(uri=BASE.has_not_completed, name="has not completed", curie=BASE.curie('has_not_completed'),
                   model_uri=BASE.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.not_completed_by = Slot(uri=BASE.not_completed_by, name="not completed by", curie=BASE.curie('not_completed_by'),
                   model_uri=BASE.not_completed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=BASE.has_completed, name="has completed", curie=BASE.curie('has_completed'),
                   model_uri=BASE.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.completed_by = Slot(uri=BASE.completed_by, name="completed by", curie=BASE.curie('completed_by'),
                   model_uri=BASE.completed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_increased_amount = Slot(uri=BASE.has_increased_amount, name="has increased amount", curie=BASE.curie('has_increased_amount'),
                   model_uri=BASE.has_increased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.increased_amount_of = Slot(uri=BASE.increased_amount_of, name="increased amount of", curie=BASE.curie('increased_amount_of'),
                   model_uri=BASE.increased_amount_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_decreased_amount = Slot(uri=BASE.has_decreased_amount, name="has decreased amount", curie=BASE.curie('has_decreased_amount'),
                   model_uri=BASE.has_decreased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreased_amount_in = Slot(uri=BASE.decreased_amount_in, name="decreased amount in", curie=BASE.curie('decreased_amount_in'),
                   model_uri=BASE.decreased_amount_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.lacks_part = Slot(uri=BASE.lacks_part, name="lacks part", curie=BASE.curie('lacks_part'),
                   model_uri=BASE.lacks_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.missing_from = Slot(uri=BASE.missing_from, name="missing from", curie=BASE.curie('missing_from'),
                   model_uri=BASE.missing_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.develops_from = Slot(uri=BASE.develops_from, name="develops from", curie=BASE.curie('develops_from'),
                   model_uri=BASE.develops_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.develops_into = Slot(uri=BASE.develops_into, name="develops into", curie=BASE.curie('develops_into'),
                   model_uri=BASE.develops_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=BASE.in_taxon, name="in taxon", curie=BASE.curie('in_taxon'),
                   model_uri=BASE.in_taxon, domain=None, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.taxon_of = Slot(uri=BASE.taxon_of, name="taxon of", curie=BASE.curie('taxon_of'),
                   model_uri=BASE.taxon_of, domain=SystemTaxon, range=Optional[Union[Union[dict, "ThingWithTaxon"], List[Union[dict, "ThingWithTaxon"]]]])

slots.has_operational_consequence = Slot(uri=BASE.has_operational_consequence, name="has operational consequence", curie=BASE.curie('has_operational_consequence'),
                   model_uri=BASE.has_operational_consequence, domain=NamedThing, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.is_operational_consequence_of = Slot(uri=BASE.is_operational_consequence_of, name="is operational consequence of", curie=BASE.curie('is_operational_consequence_of'),
                   model_uri=BASE.is_operational_consequence_of, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.association_slot = Slot(uri=BASE.association_slot, name="association slot", curie=BASE.curie('association_slot'),
                   model_uri=BASE.association_slot, domain=Association, range=Optional[str])

slots.original_subject = Slot(uri=BASE.original_subject, name="original_subject", curie=BASE.curie('original_subject'),
                   model_uri=BASE.original_subject, domain=Association, range=Optional[str])

slots.original_object = Slot(uri=BASE.original_object, name="original_object", curie=BASE.curie('original_object'),
                   model_uri=BASE.original_object, domain=Association, range=Optional[str])

slots.original_predicate = Slot(uri=BASE.original_predicate, name="original_predicate", curie=BASE.curie('original_predicate'),
                   model_uri=BASE.original_predicate, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=BASE.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=BASE.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.predicate, domain=Association, range=Union[str, PredicateType])

slots.logical_interpretation = Slot(uri=BASE.logical_interpretation, name="logical interpretation", curie=BASE.curie('logical_interpretation'),
                   model_uri=BASE.logical_interpretation, domain=Association, range=Optional[Union[str, "LogicalInterpretationEnum"]])

slots.negated = Slot(uri=BASE.negated, name="negated", curie=BASE.curie('negated'),
                   model_uri=BASE.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_confidence_level = Slot(uri=BASE.has_confidence_level, name="has confidence level", curie=BASE.curie('has_confidence_level'),
                   model_uri=BASE.has_confidence_level, domain=Association, range=Optional[Union[str, ConfidenceLevelId]])

slots.has_evidence = Slot(uri=BASE.has_evidence, name="has evidence", curie=BASE.curie('has_evidence'),
                   model_uri=BASE.has_evidence, domain=Association, range=Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]])

slots.has_supporting_study_result = Slot(uri=BASE.has_supporting_study_result, name="has supporting study result", curie=BASE.curie('has_supporting_study_result'),
                   model_uri=BASE.has_supporting_study_result, domain=Association, range=Optional[str])

slots.mechanism_of_action = Slot(uri=BASE.mechanism_of_action, name="mechanism of action", curie=BASE.curie('mechanism_of_action'),
                   model_uri=BASE.mechanism_of_action, domain=Association, range=Optional[Union[bool, Bool]])

slots.knowledge_source = Slot(uri=BASE.knowledge_source, name="knowledge source", curie=BASE.curie('knowledge_source'),
                   model_uri=BASE.knowledge_source, domain=Association, range=Optional[Union[str, InformationResourceId]])

slots.provided_by = Slot(uri=BASE.provided_by, name="provided by", curie=BASE.curie('provided_by'),
                   model_uri=BASE.provided_by, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.primary_knowledge_source = Slot(uri=BASE.primary_knowledge_source, name="primary knowledge source", curie=BASE.curie('primary_knowledge_source'),
                   model_uri=BASE.primary_knowledge_source, domain=Association, range=Optional[Union[str, InformationResourceId]])

slots.aggregator_knowledge_source = Slot(uri=BASE.aggregator_knowledge_source, name="aggregator knowledge source", curie=BASE.curie('aggregator_knowledge_source'),
                   model_uri=BASE.aggregator_knowledge_source, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.supporting_data_source = Slot(uri=BASE.supporting_data_source, name="supporting data source", curie=BASE.curie('supporting_data_source'),
                   model_uri=BASE.supporting_data_source, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.supporting_data_set = Slot(uri=BASE.supporting_data_set, name="supporting data set", curie=BASE.curie('supporting_data_set'),
                   model_uri=BASE.supporting_data_set, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.chi_squared_statistic = Slot(uri=BASE.chi_squared_statistic, name="chi squared statistic", curie=BASE.curie('chi_squared_statistic'),
                   model_uri=BASE.chi_squared_statistic, domain=Association, range=Optional[float])

slots.p_value = Slot(uri=BASE.p_value, name="p value", curie=BASE.curie('p_value'),
                   model_uri=BASE.p_value, domain=Association, range=Optional[float])

slots.evidence_count = Slot(uri=BASE.evidence_count, name="evidence count", curie=BASE.curie('evidence_count'),
                   model_uri=BASE.evidence_count, domain=Association, range=Optional[int])

slots.concept_count_subject = Slot(uri=BASE.concept_count_subject, name="concept count subject", curie=BASE.curie('concept_count_subject'),
                   model_uri=BASE.concept_count_subject, domain=Association, range=Optional[int])

slots.concept_count_object = Slot(uri=BASE.concept_count_object, name="concept count object", curie=BASE.curie('concept_count_object'),
                   model_uri=BASE.concept_count_object, domain=Association, range=Optional[int])

slots.concept_pair_count = Slot(uri=BASE.concept_pair_count, name="concept pair count", curie=BASE.curie('concept_pair_count'),
                   model_uri=BASE.concept_pair_count, domain=Association, range=Optional[int])

slots.expected_count = Slot(uri=BASE.expected_count, name="expected count", curie=BASE.curie('expected_count'),
                   model_uri=BASE.expected_count, domain=Association, range=Optional[str])

slots.relative_frequency_subject = Slot(uri=BASE.relative_frequency_subject, name="relative frequency subject", curie=BASE.curie('relative_frequency_subject'),
                   model_uri=BASE.relative_frequency_subject, domain=Association, range=Optional[float])

slots.relative_frequency_object = Slot(uri=BASE.relative_frequency_object, name="relative frequency object", curie=BASE.curie('relative_frequency_object'),
                   model_uri=BASE.relative_frequency_object, domain=Association, range=Optional[str])

slots.relative_frequency_subject_confidence_interval = Slot(uri=BASE.relative_frequency_subject_confidence_interval, name="relative frequency subject confidence interval", curie=BASE.curie('relative_frequency_subject_confidence_interval'),
                   model_uri=BASE.relative_frequency_subject_confidence_interval, domain=Association, range=Optional[str])

slots.relative_frequency_object_confidence_interval = Slot(uri=BASE.relative_frequency_object_confidence_interval, name="relative frequency object confidence interval", curie=BASE.curie('relative_frequency_object_confidence_interval'),
                   model_uri=BASE.relative_frequency_object_confidence_interval, domain=Association, range=Optional[str])

slots.adjusted_p_value = Slot(uri=BASE.adjusted_p_value, name="adjusted p value", curie=BASE.curie('adjusted_p_value'),
                   model_uri=BASE.adjusted_p_value, domain=Association, range=Optional[float])

slots.bonferonni_adjusted_p_value = Slot(uri=BASE.bonferonni_adjusted_p_value, name="bonferonni adjusted p value", curie=BASE.curie('bonferonni_adjusted_p_value'),
                   model_uri=BASE.bonferonni_adjusted_p_value, domain=Association, range=Optional[float])

slots.supporting_text = Slot(uri=BASE.supporting_text, name="supporting text", curie=BASE.curie('supporting_text'),
                   model_uri=BASE.supporting_text, domain=Association, range=Optional[Union[str, List[str]]])

slots.supporting_documents = Slot(uri=BASE.supporting_documents, name="supporting documents", curie=BASE.curie('supporting_documents'),
                   model_uri=BASE.supporting_documents, domain=Association, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.subject_location_in_text = Slot(uri=BASE.subject_location_in_text, name="subject location in text", curie=BASE.curie('subject_location_in_text'),
                   model_uri=BASE.subject_location_in_text, domain=Association, range=Optional[Union[int, List[int]]])

slots.object_location_in_text = Slot(uri=BASE.object_location_in_text, name="object location in text", curie=BASE.curie('object_location_in_text'),
                   model_uri=BASE.object_location_in_text, domain=Association, range=Optional[Union[int, List[int]]])

slots.extraction_confidence_score = Slot(uri=BASE.extraction_confidence_score, name="extraction confidence score", curie=BASE.curie('extraction_confidence_score'),
                   model_uri=BASE.extraction_confidence_score, domain=Association, range=Optional[int])

slots.supporting_document_type = Slot(uri=BASE.supporting_document_type, name="supporting document type", curie=BASE.curie('supporting_document_type'),
                   model_uri=BASE.supporting_document_type, domain=Association, range=Optional[str])

slots.supporting_document_year = Slot(uri=BASE.supporting_document_year, name="supporting document year", curie=BASE.curie('supporting_document_year'),
                   model_uri=BASE.supporting_document_year, domain=Association, range=Optional[int])

slots.supporting_text_section_type = Slot(uri=BASE.supporting_text_section_type, name="supporting text section type", curie=BASE.curie('supporting_text_section_type'),
                   model_uri=BASE.supporting_text_section_type, domain=Association, range=Optional[str])

slots.ln_ratio = Slot(uri=BASE.ln_ratio, name="ln ratio", curie=BASE.curie('ln_ratio'),
                   model_uri=BASE.ln_ratio, domain=Association, range=Optional[float])

slots.ln_ratio_confidence_interval = Slot(uri=BASE.ln_ratio_confidence_interval, name="ln ratio confidence interval", curie=BASE.curie('ln_ratio_confidence_interval'),
                   model_uri=BASE.ln_ratio_confidence_interval, domain=Association, range=Optional[float])

slots.interacting_operations_category = Slot(uri=BASE.interacting_operations_category, name="interacting operations category", curie=BASE.curie('interacting_operations_category'),
                   model_uri=BASE.interacting_operations_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.expression_site = Slot(uri=BASE.expression_site, name="expression site", curie=BASE.curie('expression_site'),
                   model_uri=BASE.expression_site, domain=Association, range=Optional[Union[str, NamedThingId]])

slots.observable_state = Slot(uri=BASE.observable_state, name="observable state", curie=BASE.curie('observable_state'),
                   model_uri=BASE.observable_state, domain=Association, range=Optional[Union[str, FaultOrObservableFeatureId]])

slots.publications = Slot(uri=BASE.publications, name="publications", curie=BASE.curie('publications'),
                   model_uri=BASE.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.associated_environmental_context = Slot(uri=BASE.associated_environmental_context, name="associated environmental context", curie=BASE.curie('associated_environmental_context'),
                   model_uri=BASE.associated_environmental_context, domain=Association, range=Optional[str])

slots.sequence_localization_attribute = Slot(uri=BASE.sequence_localization_attribute, name="sequence localization attribute", curie=BASE.curie('sequence_localization_attribute'),
                   model_uri=BASE.sequence_localization_attribute, domain=NamedThing, range=Optional[str])

slots.start_coordinate = Slot(uri=BASE.start_coordinate, name="start coordinate", curie=BASE.curie('start_coordinate'),
                   model_uri=BASE.start_coordinate, domain=NamedThing, range=Optional[int])

slots.end_coordinate = Slot(uri=BASE.end_coordinate, name="end coordinate", curie=BASE.curie('end_coordinate'),
                   model_uri=BASE.end_coordinate, domain=NamedThing, range=Optional[int])

slots.phase = Slot(uri=BASE.phase, name="phase", curie=BASE.curie('phase'),
                   model_uri=BASE.phase, domain=NamedSequence, range=Optional[Union[str, "PhaseEnum"]])

slots.regulator_approval_status = Slot(uri=BASE.regulator_approval_status, name="regulator approval status", curie=BASE.curie('regulator_approval_status'),
                   model_uri=BASE.regulator_approval_status, domain=Association, range=Optional[Union[str, "RegulatorApprovalStatusEnum"]])

slots.supporting_study_metadata = Slot(uri=BASE.supporting_study_metadata, name="supporting study metadata", curie=BASE.curie('supporting_study_metadata'),
                   model_uri=BASE.supporting_study_metadata, domain=Association, range=Optional[str])

slots.supporting_study_method_type = Slot(uri=BASE.supporting_study_method_type, name="supporting study method type", curie=BASE.curie('supporting_study_method_type'),
                   model_uri=BASE.supporting_study_method_type, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.supporting_study_method_description = Slot(uri=BASE.supporting_study_method_description, name="supporting study method description", curie=BASE.curie('supporting_study_method_description'),
                   model_uri=BASE.supporting_study_method_description, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.supporting_study_size = Slot(uri=BASE.supporting_study_size, name="supporting study size", curie=BASE.curie('supporting_study_size'),
                   model_uri=BASE.supporting_study_size, domain=Association, range=Optional[int])

slots.supporting_study_cohort = Slot(uri=BASE.supporting_study_cohort, name="supporting study cohort", curie=BASE.curie('supporting_study_cohort'),
                   model_uri=BASE.supporting_study_cohort, domain=Association, range=Optional[str])

slots.supporting_study_date_range = Slot(uri=BASE.supporting_study_date_range, name="supporting study date range", curie=BASE.curie('supporting_study_date_range'),
                   model_uri=BASE.supporting_study_date_range, domain=Association, range=Optional[str])

slots.supporting_study_context = Slot(uri=BASE.supporting_study_context, name="supporting study context", curie=BASE.curie('supporting_study_context'),
                   model_uri=BASE.supporting_study_context, domain=Association, range=Optional[str])

slots.personCollection__entries = Slot(uri=BASE.entries, name="personCollection__entries", curie=BASE.curie('entries'),
                   model_uri=BASE.personCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.Person_primary_email = Slot(uri=SCHEMA.email, name="Person_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=BASE.Person_primary_email, domain=Person, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.attribute_name = Slot(uri=RDFS.label, name="attribute_name", curie=RDFS.curie('label'),
                   model_uri=BASE.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=BASE.category, name="named thing_category", curie=BASE.curie('category'),
                   model_uri=BASE.named_thing_category, domain=NamedThing, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]],
                   pattern=re.compile(r'^base:\d+$'))

slots.system_taxon_has_taxonomic_rank = Slot(uri=BASE.has_taxonomic_rank, name="system taxon_has taxonomic rank", curie=BASE.curie('has_taxonomic_rank'),
                   model_uri=BASE.system_taxon_has_taxonomic_rank, domain=SystemTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.agent_id = Slot(uri=BASE.id, name="agent_id", curie=BASE.curie('id'),
                   model_uri=BASE.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=RDFS.label, name="agent_name", curie=RDFS.curie('label'),
                   model_uri=BASE.agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.publication_id = Slot(uri=BASE.id, name="publication_id", curie=BASE.curie('id'),
                   model_uri=BASE.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_name = Slot(uri=RDFS.label, name="publication_name", curie=RDFS.curie('label'),
                   model_uri=BASE.publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.publication_type = Slot(uri=DCT.type, name="publication_type", curie=DCT.curie('type'),
                   model_uri=BASE.publication_type, domain=Publication, range=str)

slots.publication_pages = Slot(uri=BASE.pages, name="publication_pages", curie=BASE.curie('pages'),
                   model_uri=BASE.publication_pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.book_id = Slot(uri=BASE.id, name="book_id", curie=BASE.curie('id'),
                   model_uri=BASE.book_id, domain=Book, range=Union[str, BookId])

slots.book_type = Slot(uri=RDF.type, name="book_type", curie=RDF.curie('type'),
                   model_uri=BASE.book_type, domain=Book, range=str)

slots.book_chapter_published_in = Slot(uri=BASE.published_in, name="book chapter_published in", curie=BASE.curie('published_in'),
                   model_uri=BASE.book_chapter_published_in, domain=BookChapter, range=Union[str, URIorCURIE])

slots.serial_id = Slot(uri=BASE.id, name="serial_id", curie=BASE.curie('id'),
                   model_uri=BASE.serial_id, domain=Serial, range=Union[str, SerialId])

slots.serial_type = Slot(uri=RDF.type, name="serial_type", curie=RDF.curie('type'),
                   model_uri=BASE.serial_type, domain=Serial, range=str)

slots.article_published_in = Slot(uri=BASE.published_in, name="article_published in", curie=BASE.curie('published_in'),
                   model_uri=BASE.article_published_in, domain=Article, range=Union[str, URIorCURIE])

slots.article_iso_abbreviation = Slot(uri=BASE.iso_abbreviation, name="article_iso abbreviation", curie=BASE.curie('iso_abbreviation'),
                   model_uri=BASE.article_iso_abbreviation, domain=Article, range=Optional[str])

slots.operational_activity_has_input = Slot(uri=BASE.has_input, name="operational activity_has input", curie=BASE.curie('has_input'),
                   model_uri=BASE.operational_activity_has_input, domain=OperationalActivity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.operational_activity_has_output = Slot(uri=BASE.has_output, name="operational activity_has output", curie=BASE.curie('has_output'),
                   model_uri=BASE.operational_activity_has_output, domain=OperationalActivity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.operational_activity_enabled_by = Slot(uri=BASE.enabled_by, name="operational activity_enabled by", curie=BASE.curie('enabled_by'),
                   model_uri=BASE.operational_activity_enabled_by, domain=OperationalActivity, range=Optional[Union[Union[dict, "AssemblyMixin"], List[Union[dict, "AssemblyMixin"]]]])

slots.system_entity_has_attribute = Slot(uri=BASE.has_attribute, name="system entity_has attribute", curie=BASE.curie('has_attribute'),
                   model_uri=BASE.system_entity_has_attribute, domain=SystemEntity, range=Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]])

slots.assembly_mixin_name = Slot(uri=RDFS.label, name="assembly mixin_name", curie=RDFS.curie('label'),
                   model_uri=BASE.assembly_mixin_name, domain=None, range=Optional[Union[str, SymbolType]])

slots.empirical_measurement_has_attribute_type = Slot(uri=BASE.has_attribute_type, name="empirical measurement_has attribute type", curie=BASE.curie('has_attribute_type'),
                   model_uri=BASE.empirical_measurement_has_attribute_type, domain=EmpiricalMeasurement, range=Union[str, OntologyClassId])

slots.empirical_finding_has_attribute = Slot(uri=BASE.has_attribute, name="empirical finding_has attribute", curie=BASE.curie('has_attribute'),
                   model_uri=BASE.empirical_finding_has_attribute, domain=EmpiricalFinding, range=Optional[Union[Union[str, EmpiricalAttributeId], List[Union[str, EmpiricalAttributeId]]]])

slots.socioeconomic_exposure_has_attribute = Slot(uri=BASE.has_attribute, name="socioeconomic exposure_has attribute", curie=BASE.curie('has_attribute'),
                   model_uri=BASE.socioeconomic_exposure_has_attribute, domain=SocioeconomicExposure, range=Union[Union[str, SocioeconomicAttributeId], List[Union[str, SocioeconomicAttributeId]]])

slots.association_type = Slot(uri=RDF.type, name="association_type", curie=RDF.curie('type'),
                   model_uri=BASE.association_type, domain=Association, range=Optional[str])

slots.association_category = Slot(uri=BASE.category, name="association_category", curie=BASE.curie('category'),
                   model_uri=BASE.association_category, domain=Association, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])

slots.control_entity_assesses_named_thing_association_subject = Slot(uri=RDF.subject, name="control entity assesses named thing association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.control_entity_assesses_named_thing_association_subject, domain=ControlEntityAssessesNamedThingAssociation, range=Union[str, ControlEntityId])

slots.control_entity_assesses_named_thing_association_object = Slot(uri=RDF.object, name="control entity assesses named thing association_object", curie=RDF.curie('object'),
                   model_uri=BASE.control_entity_assesses_named_thing_association_object, domain=ControlEntityAssessesNamedThingAssociation, range=Union[str, NamedThingId])

slots.control_entity_assesses_named_thing_association_predicate = Slot(uri=RDF.predicate, name="control entity assesses named thing association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.control_entity_assesses_named_thing_association_predicate, domain=ControlEntityAssessesNamedThingAssociation, range=Union[str, PredicateType])

slots.contributor_association_subject = Slot(uri=RDF.subject, name="contributor association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.contributor_association_subject, domain=ContributorAssociation, range=Union[str, InformationContentEntityId])

slots.contributor_association_predicate = Slot(uri=RDF.predicate, name="contributor association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.contributor_association_predicate, domain=ContributorAssociation, range=Union[str, PredicateType])

slots.contributor_association_object = Slot(uri=RDF.object, name="contributor association_object", curie=RDF.curie('object'),
                   model_uri=BASE.contributor_association_object, domain=ContributorAssociation, range=Union[str, AgentId])

slots.contributor_association_qualifiers = Slot(uri=BASE.qualifiers, name="contributor association_qualifiers", curie=BASE.curie('qualifiers'),
                   model_uri=BASE.contributor_association_qualifiers, domain=ContributorAssociation, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.service_type_to_service_type_part_association_predicate = Slot(uri=RDF.predicate, name="service type to service type part association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.service_type_to_service_type_part_association_predicate, domain=ServiceTypeToServiceTypePartAssociation, range=Union[str, PredicateType])

slots.service_type_to_service_type_part_association_subject = Slot(uri=RDF.subject, name="service type to service type part association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.service_type_to_service_type_part_association_subject, domain=ServiceTypeToServiceTypePartAssociation, range=Union[str, ServiceTypeId])

slots.service_type_to_service_type_part_association_object = Slot(uri=RDF.object, name="service type to service type part association_object", curie=RDF.curie('object'),
                   model_uri=BASE.service_type_to_service_type_part_association_object, domain=ServiceTypeToServiceTypePartAssociation, range=Union[str, ServiceTypeId])

slots.service_type_to_class_association_predicate = Slot(uri=RDF.predicate, name="service type to class association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.service_type_to_class_association_predicate, domain=ServiceTypeToClassAssociation, range=Union[str, PredicateType])

slots.service_type_to_class_association_subject = Slot(uri=RDF.subject, name="service type to class association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.service_type_to_class_association_subject, domain=ServiceTypeToClassAssociation, range=Union[str, ServiceTypeId])

slots.service_type_to_class_association_object = Slot(uri=RDF.object, name="service type to class association_object", curie=RDF.curie('object'),
                   model_uri=BASE.service_type_to_class_association_object, domain=ServiceTypeToClassAssociation, range=Union[str, ClassId])

slots.class_to_class_association_subject = Slot(uri=RDF.subject, name="class to class association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.class_to_class_association_subject, domain=ClassToClassAssociation, range=Union[dict, ClassOrSubclasses])

slots.class_to_class_association_object = Slot(uri=RDF.object, name="class to class association_object", curie=RDF.curie('object'),
                   model_uri=BASE.class_to_class_association_object, domain=ClassToClassAssociation, range=Union[dict, ClassOrSubclasses])

slots.component_type_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="component type to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.component_type_to_entity_association_mixin_subject, domain=None, range=Union[str, ComponentTypeId])

slots.control_entity_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="control entity to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.control_entity_to_entity_association_mixin_subject, domain=None, range=Union[dict, ControlEntityOrClassOrSubclasses])

slots.administrative_operation_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="administrative operation to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.administrative_operation_to_entity_association_mixin_subject, domain=None, range=Union[str, AdministrativeOperationId])

slots.control_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="control to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.control_to_entity_association_mixin_subject, domain=None, range=Union[dict, ControlEntityOrClassOrSubclasses])

slots.case_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="case to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.case_to_entity_association_mixin_subject, domain=None, range=Union[str, CaseId])

slots.control_to_control_association_object = Slot(uri=RDF.object, name="control to control association_object", curie=RDF.curie('object'),
                   model_uri=BASE.control_to_control_association_object, domain=ControlToControlAssociation, range=Union[str, ControlEntityId])

slots.reaction_to_participant_association_subject = Slot(uri=RDF.subject, name="reaction to participant association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.reaction_to_participant_association_subject, domain=ReactionToParticipantAssociation, range=Union[str, OperationalEntityId])

slots.reaction_to_catalyst_association_object = Slot(uri=RDF.object, name="reaction to catalyst association_object", curie=RDF.curie('object'),
                   model_uri=BASE.reaction_to_catalyst_association_object, domain=ReactionToCatalystAssociation, range=Union[dict, ClassOrSubclasses])

slots.control_to_fault_or_observable_feature_association_object = Slot(uri=RDF.object, name="control to fault or observable feature association_object", curie=RDF.curie('object'),
                   model_uri=BASE.control_to_fault_or_observable_feature_association_object, domain=ControlToFaultOrObservableFeatureAssociation, range=Union[str, FaultOrObservableFeatureId])

slots.class_to_pathway_association_subject = Slot(uri=RDF.subject, name="class to pathway association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.class_to_pathway_association_subject, domain=ClassToPathwayAssociation, range=Union[dict, ClassOrSubclasses])

slots.class_to_pathway_association_object = Slot(uri=RDF.object, name="class to pathway association_object", curie=RDF.curie('object'),
                   model_uri=BASE.class_to_pathway_association_object, domain=ClassToPathwayAssociation, range=Union[str, PathwayId])

slots.operational_activity_to_pathway_association_subject = Slot(uri=RDF.subject, name="operational activity to pathway association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.operational_activity_to_pathway_association_subject, domain=OperationalActivityToPathwayAssociation, range=Union[str, OperationalActivityId])

slots.operational_activity_to_pathway_association_object = Slot(uri=RDF.object, name="operational activity to pathway association_object", curie=RDF.curie('object'),
                   model_uri=BASE.operational_activity_to_pathway_association_object, domain=OperationalActivityToPathwayAssociation, range=Union[str, PathwayId])

slots.operational_activity_to_pathway_association_predicate = Slot(uri=RDF.predicate, name="operational activity to pathway association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.operational_activity_to_pathway_association_predicate, domain=OperationalActivityToPathwayAssociation, range=Union[str, PredicateType])

slots.control_to_pathway_association_subject = Slot(uri=RDF.subject, name="control to pathway association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.control_to_pathway_association_subject, domain=ControlToPathwayAssociation, range=Union[str, ControlEntityId])

slots.control_to_pathway_association_object = Slot(uri=RDF.object, name="control to pathway association_object", curie=RDF.curie('object'),
                   model_uri=BASE.control_to_pathway_association_object, domain=ControlToPathwayAssociation, range=Union[str, PathwayId])

slots.administrative_operation_to_class_association_object = Slot(uri=RDF.object, name="administrative operation to class association_object", curie=RDF.curie('object'),
                   model_uri=BASE.administrative_operation_to_class_association_object, domain=AdministrativeOperationToClassAssociation, range=Union[dict, ClassOrSubclasses])

slots.fault_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="fault to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.fault_to_entity_association_mixin_subject, domain=None, range=Union[str, FaultId])

slots.entity_to_exposure_event_association_mixin_object = Slot(uri=RDF.object, name="entity to exposure event association mixin_object", curie=RDF.curie('object'),
                   model_uri=BASE.entity_to_exposure_event_association_mixin_object, domain=None, range=Union[str, ExposureEventId])

slots.entity_to_outcome_association_mixin_object = Slot(uri=RDF.object, name="entity to outcome association mixin_object", curie=RDF.curie('object'),
                   model_uri=BASE.entity_to_outcome_association_mixin_object, domain=None, range=Union[dict, Outcome])

slots.entity_to_observable_feature_association_mixin_object = Slot(uri=RDF.object, name="entity to observable feature association mixin_object", curie=RDF.curie('object'),
                   model_uri=BASE.entity_to_observable_feature_association_mixin_object, domain=None, range=Union[str, ObservableFeatureId])

slots.information_content_entity_to_named_thing_association_subject = Slot(uri=RDF.subject, name="information content entity to named thing association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.information_content_entity_to_named_thing_association_subject, domain=InformationContentEntityToNamedThingAssociation, range=Union[str, NamedThingId])

slots.information_content_entity_to_named_thing_association_object = Slot(uri=RDF.object, name="information content entity to named thing association_object", curie=RDF.curie('object'),
                   model_uri=BASE.information_content_entity_to_named_thing_association_object, domain=InformationContentEntityToNamedThingAssociation, range=Union[str, NamedThingId])

slots.information_content_entity_to_named_thing_association_predicate = Slot(uri=RDF.predicate, name="information content entity to named thing association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.information_content_entity_to_named_thing_association_predicate, domain=InformationContentEntityToNamedThingAssociation, range=Union[str, PredicateType])

slots.entity_to_fault_association_mixin_object = Slot(uri=RDF.object, name="entity to fault association mixin_object", curie=RDF.curie('object'),
                   model_uri=BASE.entity_to_fault_association_mixin_object, domain=None, range=Union[str, FaultId])

slots.fault_or_observable_feature_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="fault or observable feature to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.fault_or_observable_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, FaultOrObservableFeatureId])

slots.fault_or_observable_feature_to_location_association_object = Slot(uri=RDF.object, name="fault or observable feature to location association_object", curie=RDF.curie('object'),
                   model_uri=BASE.fault_or_observable_feature_to_location_association_object, domain=FaultOrObservableFeatureToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.entity_to_fault_or_observable_feature_association_mixin_object = Slot(uri=RDF.object, name="entity to fault or observable feature association mixin_object", curie=RDF.curie('object'),
                   model_uri=BASE.entity_to_fault_or_observable_feature_association_mixin_object, domain=None, range=Union[str, FaultOrObservableFeatureId])

slots.service_type_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="service type to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.service_type_to_entity_association_mixin_subject, domain=None, range=Union[str, ServiceTypeId])

slots.service_type_to_observable_feature_association_predicate = Slot(uri=RDF.predicate, name="service type to observable feature association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.service_type_to_observable_feature_association_predicate, domain=ServiceTypeToObservableFeatureAssociation, range=Union[str, PredicateType])

slots.service_type_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="service type to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.service_type_to_observable_feature_association_subject, domain=ServiceTypeToObservableFeatureAssociation, range=Union[str, ServiceTypeId])

slots.exposure_event_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="exposure event to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.exposure_event_to_observable_feature_association_subject, domain=ExposureEventToObservableFeatureAssociation, range=Union[str, ExposureEventId])

slots.fault_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="fault to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.fault_to_observable_feature_association_subject, domain=FaultToObservableFeatureAssociation, range=Union[str, FaultId])

slots.fault_to_observable_feature_association_object = Slot(uri=RDF.object, name="fault to observable feature association_object", curie=RDF.curie('object'),
                   model_uri=BASE.fault_to_observable_feature_association_object, domain=FaultToObservableFeatureAssociation, range=Union[str, ObservableFeatureId])

slots.behavior_to_behavioral_feature_association_subject = Slot(uri=RDF.subject, name="behavior to behavioral feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.behavior_to_behavioral_feature_association_subject, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehaviorId])

slots.behavior_to_behavioral_feature_association_object = Slot(uri=RDF.object, name="behavior to behavioral feature association_object", curie=RDF.curie('object'),
                   model_uri=BASE.behavior_to_behavioral_feature_association_object, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehavioralFeatureId])

slots.class_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="class to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.class_to_entity_association_mixin_subject, domain=None, range=Union[dict, ClassOrSubclasses])

slots.class_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="class to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.class_to_observable_feature_association_subject, domain=ClassToObservableFeatureAssociation, range=Union[dict, ClassOrSubclasses])

slots.class_to_observable_feature_association_object = Slot(uri=RDF.object, name="class to observable feature association_object", curie=RDF.curie('object'),
                   model_uri=BASE.class_to_observable_feature_association_object, domain=ClassToObservableFeatureAssociation, range=Union[str, ObservableFeatureId])

slots.class_to_fault_association_subject = Slot(uri=RDF.subject, name="class to fault association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.class_to_fault_association_subject, domain=ClassToFaultAssociation, range=Union[dict, ClassOrSubclasses])

slots.class_to_fault_association_object = Slot(uri=RDF.object, name="class to fault association_object", curie=RDF.curie('object'),
                   model_uri=BASE.class_to_fault_association_object, domain=ClassToFaultAssociation, range=Union[str, FaultId])

slots.controllable_class_to_fault_association_subject = Slot(uri=RDF.subject, name="controllable class to fault association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.controllable_class_to_fault_association_subject, domain=ControllableClassToFaultAssociation, range=Union[dict, ClassOrSubclasses])

slots.controllable_class_to_fault_association_predicate = Slot(uri=RDF.predicate, name="controllable class to fault association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.controllable_class_to_fault_association_predicate, domain=ControllableClassToFaultAssociation, range=Union[str, PredicateType])

slots.controllable_class_to_fault_association_has_evidence = Slot(uri=BASE.has_evidence, name="controllable class to fault association_has evidence", curie=BASE.curie('has_evidence'),
                   model_uri=BASE.controllable_class_to_fault_association_has_evidence, domain=ControllableClassToFaultAssociation, range=Optional[Union[Union[str, "ControllableClassCategoryEnum"], List[Union[str, "ControllableClassCategoryEnum"]]]])

slots.population_to_population_association_subject = Slot(uri=RDF.subject, name="population to population association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_object = Slot(uri=RDF.object, name="population to population association_object", curie=RDF.curie('object'),
                   model_uri=BASE.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_predicate = Slot(uri=RDF.predicate, name="population to population association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.population_to_population_association_predicate, domain=PopulationToPopulationAssociation, range=Union[str, PredicateType])

slots.service_type_to_fault_association_subject = Slot(uri=RDF.subject, name="service type to fault association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.service_type_to_fault_association_subject, domain=ServiceTypeToFaultAssociation, range=Union[str, NamedThingId])

slots.service_type_to_fault_association_predicate = Slot(uri=RDF.predicate, name="service type to fault association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.service_type_to_fault_association_predicate, domain=ServiceTypeToFaultAssociation, range=Union[str, PredicateType])

slots.service_type_to_fault_association_object = Slot(uri=RDF.object, name="service type to fault association_object", curie=RDF.curie('object'),
                   model_uri=BASE.service_type_to_fault_association_object, domain=ServiceTypeToFaultAssociation, range=Union[str, NamedThingId])

slots.system_to_system_association_subject = Slot(uri=RDF.subject, name="system to system association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.system_to_system_association_subject, domain=SystemToSystemAssociation, range=Union[str, IndividualSystemId])

slots.system_to_system_association_object = Slot(uri=RDF.object, name="system to system association_object", curie=RDF.curie('object'),
                   model_uri=BASE.system_to_system_association_object, domain=SystemToSystemAssociation, range=Union[str, IndividualSystemId])

slots.taxon_to_taxon_association_subject = Slot(uri=RDF.subject, name="taxon to taxon association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.taxon_to_taxon_association_subject, domain=TaxonToTaxonAssociation, range=Union[str, SystemTaxonId])

slots.taxon_to_taxon_association_object = Slot(uri=RDF.object, name="taxon to taxon association_object", curie=RDF.curie('object'),
                   model_uri=BASE.taxon_to_taxon_association_object, domain=TaxonToTaxonAssociation, range=Union[str, SystemTaxonId])

slots.class_to_expression_site_association_subject = Slot(uri=RDF.subject, name="class to expression site association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.class_to_expression_site_association_subject, domain=ClassToExpressionSiteAssociation, range=Union[dict, ClassOrSubclasses])

slots.class_to_expression_site_association_object = Slot(uri=RDF.object, name="class to expression site association_object", curie=RDF.curie('object'),
                   model_uri=BASE.class_to_expression_site_association_object, domain=ClassToExpressionSiteAssociation, range=Union[str, DeploymentEntityId])

slots.class_to_expression_site_association_predicate = Slot(uri=RDF.predicate, name="class to expression site association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BASE.class_to_expression_site_association_predicate, domain=ClassToExpressionSiteAssociation, range=Union[str, PredicateType])

slots.class_to_expression_site_association_stage_qualifier = Slot(uri=BASE.stage_qualifier, name="class to expression site association_stage qualifier", curie=BASE.curie('stage_qualifier'),
                   model_uri=BASE.class_to_expression_site_association_stage_qualifier, domain=ClassToExpressionSiteAssociation, range=Optional[Union[str, LifecycleStageId]])

slots.class_to_expression_site_association_quantifier_qualifier = Slot(uri=BASE.quantifier_qualifier, name="class to expression site association_quantifier qualifier", curie=BASE.curie('quantifier_qualifier'),
                   model_uri=BASE.class_to_expression_site_association_quantifier_qualifier, domain=ClassToExpressionSiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.functional_association_subject = Slot(uri=RDF.subject, name="functional association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.functional_association_subject, domain=FunctionalAssociation, range=Union[dict, AssemblyMixin])

slots.functional_association_object = Slot(uri=RDF.object, name="functional association_object", curie=RDF.curie('object'),
                   model_uri=BASE.functional_association_object, domain=FunctionalAssociation, range=Union[str, OntologyClassId])

slots.assembly_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="assembly to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.assembly_to_entity_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.assembly_to_operational_activity_association_object = Slot(uri=RDF.object, name="assembly to operational activity association_object", curie=RDF.curie('object'),
                   model_uri=BASE.assembly_to_operational_activity_association_object, domain=AssemblyToOperationalActivityAssociation, range=Union[str, OperationalActivityId])

slots.assembly_to_computational_process_association_object = Slot(uri=RDF.object, name="assembly to computational process association_object", curie=RDF.curie('object'),
                   model_uri=BASE.assembly_to_computational_process_association_object, domain=AssemblyToComputationalProcessAssociation, range=Union[str, ComputationalProcessId])

slots.assembly_to_component_association_object = Slot(uri=RDF.object, name="assembly to component association_object", curie=RDF.curie('object'),
                   model_uri=BASE.assembly_to_component_association_object, domain=AssemblyToComponentAssociation, range=Union[str, ComponentId])

slots.system_taxon_to_entity_association_subject = Slot(uri=RDF.subject, name="system taxon to entity association_subject", curie=RDF.curie('subject'),
                   model_uri=BASE.system_taxon_to_entity_association_subject, domain=None, range=Union[str, SystemTaxonId])