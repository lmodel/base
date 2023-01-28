

CREATE TABLE activity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE agent (
	iri TEXT, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	address TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE article (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT NOT NULL, 
	published_in TEXT NOT NULL, 
	iso_abbreviation TEXT, 
	volume TEXT, 
	issue TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE assembly_complex (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE behavior (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE behavioral_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE book (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	summary TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE book_chapter (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT NOT NULL, 
	published_in TEXT NOT NULL, 
	volume TEXT, 
	chapter TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "case" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE chi_squared_analysis_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE class (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	symbol TEXT, 
	has_computational_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cohort (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE common_data_element (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE component (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE component_system (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE component_type (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE computational_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE computational_process_or_activity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE confidence_level (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE control_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id)
);

CREATE TABLE dataset (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE dataset_distribution (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	distribution_download_url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE dataset_summary (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	source_web_page TEXT, 
	source_logo TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE deployment_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE empirical_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE empirical_finding (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE empirical_intervention (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE environmental_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE environmental_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE event (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE evidence_type (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE fault (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE fault_or_observable_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE fault_or_observable_feature_exposure (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id)
);

CREATE TABLE faulty_deployment_structure (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE faulty_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE geographic_location (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (id)
);

CREATE TABLE geographic_location_at_time (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	timepoint TIME, 
	PRIMARY KEY (id)
);

CREATE TABLE individual_system (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE information_resource (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE inheritance (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE lifecycle_stage (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE material_sample (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE named_sequence (
	has_computational_sequence TEXT, 
	PRIMARY KEY (has_computational_sequence)
);

CREATE TABLE named_thing (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE observable_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE offline_maintenance (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE operational_activity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE pathway (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	PRIMARY KEY (id)
);

CREATE TABLE "PersonCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE phenomenon (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE physical_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE planetary_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE population_of_individual_systems (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE publication (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE quantity_value (
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	PRIMARY KEY (has_unit, has_numeric_value)
);

CREATE TABLE relationship_type (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE restoration (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id)
);

CREATE TABLE serial (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	summary TEXT, 
	name TEXT, 
	iso_abbreviation TEXT, 
	volume TEXT, 
	issue TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE study (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE study_population (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	in_taxon TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE study_variable (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE system_operation (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE system_operation_domain (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_class_or_subclasses TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE taxonomic_rank (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE text_mining_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE workload (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_computational_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE administrative_operation_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_quantitative_value TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE administrative_operation_to_class_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id)
);

CREATE TABLE assembly_to_component_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES component (id)
);

CREATE TABLE assembly_to_computational_process_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES computational_process (id)
);

CREATE TABLE assembly_to_operational_activity_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES operational_activity (id)
);

CREATE TABLE association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id)
);

CREATE TABLE attribute (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE behavioral_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE biological_sex (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE class_to_expression_site_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	stage_qualifier TEXT, 
	quantifier_qualifier TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(stage_qualifier) REFERENCES lifecycle_stage (id), 
	FOREIGN KEY(object) REFERENCES deployment_entity (id)
);

CREATE TABLE class_to_pathway_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES pathway (id)
);

CREATE TABLE contributor_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES agent (id)
);

CREATE TABLE control_entity_assesses_named_thing_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES control_entity (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE control_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_quantitative_value TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE control_mixture (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_supplement TEXT, 
	highest_regulator_approval_status TEXT, 
	administrative_operation_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES control_mixture (id)
);

CREATE TABLE control_role (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE control_to_control_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES control_entity (id)
);

CREATE TABLE control_to_fault_or_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES fault_or_observable_feature (id)
);

CREATE TABLE control_to_pathway_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES control_entity (id), 
	FOREIGN KEY(object) REFERENCES pathway (id)
);

CREATE TABLE dataset_version (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	has_dataset TEXT, 
	ingest_date TEXT, 
	has_distribution TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_dataset) REFERENCES dataset (id), 
	FOREIGN KEY(has_distribution) REFERENCES dataset_distribution (id)
);

CREATE TABLE device (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	restoration_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(restoration_id) REFERENCES restoration (id)
);

CREATE TABLE empirical_attribute (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	empirical_finding_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id), 
	FOREIGN KEY(empirical_finding_id) REFERENCES empirical_finding (id)
);

CREATE TABLE empirical_course (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE empirical_measurement (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_attribute_type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE empirical_modifier (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE entity_to_fault_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	regulator_approval_status VARCHAR(1), 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id)
);

CREATE TABLE entity_to_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	regulator_approval_status VARCHAR(1), 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id)
);

CREATE TABLE environmental_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE exposure_event_to_outcome_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	population_context_qualifier TEXT, 
	temporal_context_qualifier TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(population_context_qualifier) REFERENCES population_of_individual_systems (id)
);

CREATE TABLE fault_or_observable_feature_to_location_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES deployment_entity (id)
);

CREATE TABLE fault_to_exposure_event_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id)
);

CREATE TABLE faulty_deployment_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE faulty_process_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE functional_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id)
);

CREATE TABLE geographic_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE homogeneity (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE information_content_entity_to_named_thing_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE observable_quality (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE onset (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE operational_activity_to_pathway_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES operational_activity (id), 
	FOREIGN KEY(object) REFERENCES pathway (id)
);

CREATE TABLE operational_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_controller BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id)
);

CREATE TABLE population_to_population_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES population_of_individual_systems (id), 
	FOREIGN KEY(object) REFERENCES population_of_individual_systems (id)
);

CREATE TABLE procedure (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	restoration_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(restoration_id) REFERENCES restoration (id)
);

CREATE TABLE redundancy_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_controller BOOLEAN, 
	has_computational_sequence TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id)
);

CREATE TABLE replica (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_controller BOOLEAN, 
	has_computational_sequence TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id)
);

CREATE TABLE severity_value (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE socioeconomic_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE system_attribute (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE system_taxon (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	has_taxonomic_rank TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_taxonomic_rank) REFERENCES taxonomic_rank (id)
);

CREATE TABLE system_to_system_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES individual_system (id), 
	FOREIGN KEY(object) REFERENCES individual_system (id)
);

CREATE TABLE workload_background_exposure (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	has_class_or_subclasses TEXT, 
	has_computational_sequence TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE activity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE activity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE agent_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_affiliation (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE article_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE assembly_complex_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES assembly_complex (id)
);

CREATE TABLE assembly_complex_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES assembly_complex (id)
);

CREATE TABLE assembly_complex_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES assembly_complex (id)
);

CREATE TABLE behavior_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavioral_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE behavioral_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE behavioral_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE book_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_chapter_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE case_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE case_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE case_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE chi_squared_analysis_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE chi_squared_analysis_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE chi_squared_analysis_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE class_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES class (id)
);

CREATE TABLE class_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES class (id)
);

CREATE TABLE class_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES class (id)
);

CREATE TABLE class_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES class (id)
);

CREATE TABLE cohort_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE cohort_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE cohort_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE common_data_element_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE common_data_element_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE common_data_element_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE component_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES component (id)
);

CREATE TABLE component_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES component (id)
);

CREATE TABLE component_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES component (id)
);

CREATE TABLE component_system_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES component_system (id)
);

CREATE TABLE component_system_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES component_system (id)
);

CREATE TABLE component_system_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES component_system (id)
);

CREATE TABLE component_type_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES component_type (id)
);

CREATE TABLE component_type_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES component_type (id)
);

CREATE TABLE component_type_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES component_type (id)
);

CREATE TABLE computational_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES computational_process (id)
);

CREATE TABLE computational_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES computational_process (id)
);

CREATE TABLE computational_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES computational_process (id)
);

CREATE TABLE computational_process_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES computational_process (id)
);

CREATE TABLE computational_process_or_activity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES computational_process_or_activity (id)
);

CREATE TABLE computational_process_or_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES computational_process_or_activity (id)
);

CREATE TABLE computational_process_or_activity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES computational_process_or_activity (id)
);

CREATE TABLE computational_process_or_activity_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES computational_process_or_activity (id)
);

CREATE TABLE confidence_level_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE confidence_level_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE confidence_level_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE control_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES control_entity (id)
);

CREATE TABLE control_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES control_entity (id)
);

CREATE TABLE control_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_entity (id)
);

CREATE TABLE dataset_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_distribution_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_distribution_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_distribution_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_summary_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE dataset_summary_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE dataset_summary_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE deployment_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES deployment_entity (id)
);

CREATE TABLE deployment_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES deployment_entity (id)
);

CREATE TABLE deployment_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES deployment_entity (id)
);

CREATE TABLE empirical_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_entity (id)
);

CREATE TABLE empirical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_entity (id)
);

CREATE TABLE empirical_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_entity (id)
);

CREATE TABLE empirical_finding_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_finding (id)
);

CREATE TABLE empirical_finding_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_finding (id)
);

CREATE TABLE empirical_finding_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_finding (id)
);

CREATE TABLE empirical_intervention_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_intervention (id)
);

CREATE TABLE empirical_intervention_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_intervention (id)
);

CREATE TABLE empirical_intervention_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_intervention (id)
);

CREATE TABLE environmental_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE environmental_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE environmental_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE event_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE event_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE event_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE evidence_type_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE evidence_type_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE evidence_type_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE fault_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES fault (id)
);

CREATE TABLE fault_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES fault (id)
);

CREATE TABLE fault_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fault (id)
);

CREATE TABLE fault_or_observable_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature (id)
);

CREATE TABLE fault_or_observable_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature (id)
);

CREATE TABLE fault_or_observable_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature (id)
);

CREATE TABLE fault_or_observable_feature_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature_exposure (id)
);

CREATE TABLE fault_or_observable_feature_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature_exposure (id)
);

CREATE TABLE fault_or_observable_feature_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature_exposure (id)
);

CREATE TABLE faulty_deployment_structure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES faulty_deployment_structure (id)
);

CREATE TABLE faulty_deployment_structure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES faulty_deployment_structure (id)
);

CREATE TABLE faulty_deployment_structure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES faulty_deployment_structure (id)
);

CREATE TABLE faulty_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process (id)
);

CREATE TABLE faulty_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process (id)
);

CREATE TABLE faulty_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process (id)
);

CREATE TABLE faulty_process_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process (id)
);

CREATE TABLE geographic_location_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_at_time_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE geographic_location_at_time_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE geographic_location_at_time_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE individual_system_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES individual_system (id)
);

CREATE TABLE individual_system_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES individual_system (id)
);

CREATE TABLE individual_system_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES individual_system (id)
);

CREATE TABLE information_resource_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES information_resource (id)
);

CREATE TABLE information_resource_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES information_resource (id)
);

CREATE TABLE information_resource_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES information_resource (id)
);

CREATE TABLE inheritance_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES inheritance (id)
);

CREATE TABLE inheritance_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES inheritance (id)
);

CREATE TABLE inheritance_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES inheritance (id)
);

CREATE TABLE lifecycle_stage_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES lifecycle_stage (id)
);

CREATE TABLE lifecycle_stage_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES lifecycle_stage (id)
);

CREATE TABLE lifecycle_stage_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES lifecycle_stage (id)
);

CREATE TABLE material_sample_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE material_sample_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE material_sample_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE named_thing_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE named_thing_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE named_thing_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE observable_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES observable_feature (id)
);

CREATE TABLE observable_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES observable_feature (id)
);

CREATE TABLE observable_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES observable_feature (id)
);

CREATE TABLE offline_maintenance_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES offline_maintenance (id)
);

CREATE TABLE offline_maintenance_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES offline_maintenance (id)
);

CREATE TABLE offline_maintenance_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES offline_maintenance (id)
);

CREATE TABLE operational_activity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES operational_activity (id)
);

CREATE TABLE operational_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES operational_activity (id)
);

CREATE TABLE operational_activity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES operational_activity (id)
);

CREATE TABLE operational_activity_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES operational_activity (id)
);

CREATE TABLE pathway_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE phenomenon_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenomenon_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenomenon_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE physical_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physical_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE planetary_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE planetary_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE planetary_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE population_of_individual_systems_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_systems (id)
);

CREATE TABLE population_of_individual_systems_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_systems (id)
);

CREATE TABLE population_of_individual_systems_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_systems (id)
);

CREATE TABLE publication_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE restoration_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES restoration (id)
);

CREATE TABLE restoration_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES restoration (id)
);

CREATE TABLE restoration_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES restoration (id)
);

CREATE TABLE serial_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE study_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_population_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_population_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_population_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_variable_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE study_variable_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE study_variable_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE system_operation_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES system_operation (id)
);

CREATE TABLE system_operation_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES system_operation (id)
);

CREATE TABLE system_operation_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES system_operation (id)
);

CREATE TABLE system_operation_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES system_operation (id)
);

CREATE TABLE system_operation_domain_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES system_operation_domain (id)
);

CREATE TABLE system_operation_domain_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES system_operation_domain (id)
);

CREATE TABLE system_operation_domain_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES system_operation_domain (id)
);

CREATE TABLE text_mining_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE text_mining_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE text_mining_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE workload_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES workload (id)
);

CREATE TABLE workload_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES workload (id)
);

CREATE TABLE workload_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES workload (id)
);

CREATE TABLE administrative_operation (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_supplement TEXT, 
	highest_regulator_approval_status TEXT, 
	administrative_operation_regulatory_status_world_wide TEXT, 
	restoration_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES control_mixture (id), 
	FOREIGN KEY(restoration_id) REFERENCES restoration (id)
);

CREATE TABLE behavior_to_behavioral_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES behavior (id), 
	FOREIGN KEY(object) REFERENCES behavioral_feature (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE case_to_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE class_to_fault_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES fault (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE class_to_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES observable_feature (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE complex_operational_mixture (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_supplement TEXT, 
	highest_regulator_approval_status TEXT, 
	administrative_operation_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES control_mixture (id)
);

CREATE TABLE controllable_class_to_fault_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES fault (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE exposure_event_to_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE fault_to_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES fault (id), 
	FOREIGN KEY(object) REFERENCES observable_feature (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE operational_mixture (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_supplement TEXT, 
	highest_regulator_approval_status TEXT, 
	administrative_operation_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES control_mixture (id)
);

CREATE TABLE processed_material (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	trade_name TEXT, 
	available_from TEXT, 
	is_toxic BOOLEAN, 
	has_control_role TEXT, 
	is_supplement TEXT, 
	highest_regulator_approval_status TEXT, 
	administrative_operation_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES control_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES control_mixture (id)
);

CREATE TABLE reaction_to_catalyst_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	ratios INTEGER, 
	reaction_direction VARCHAR(13), 
	reaction_side VARCHAR(5), 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES operational_entity (id)
);

CREATE TABLE reaction_to_participant_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	object TEXT NOT NULL, 
	ratios INTEGER, 
	reaction_direction VARCHAR(13), 
	reaction_side VARCHAR(5), 
	subject TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(object) REFERENCES control_entity (id), 
	FOREIGN KEY(subject) REFERENCES operational_entity (id)
);

CREATE TABLE service_type (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	has_homogeneity TEXT, 
	has_computational_sequence TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_homogeneity) REFERENCES homogeneity (id)
);

CREATE TABLE service_type_to_fault_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE socioeconomic_attribute (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	socioeconomic_exposure_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id), 
	FOREIGN KEY(socioeconomic_exposure_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE taxon_to_taxon_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES system_taxon (id), 
	FOREIGN KEY(object) REFERENCES system_taxon (id)
);

CREATE TABLE administrative_operation_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation_exposure (id)
);

CREATE TABLE administrative_operation_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation_exposure (id)
);

CREATE TABLE administrative_operation_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation_exposure (id)
);

CREATE TABLE administrative_operation_to_class_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation_to_class_association (id)
);

CREATE TABLE administrative_operation_to_class_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation_to_class_association (id)
);

CREATE TABLE assembly_to_component_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES assembly_to_component_association (id)
);

CREATE TABLE assembly_to_component_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES assembly_to_component_association (id)
);

CREATE TABLE assembly_to_computational_process_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES assembly_to_computational_process_association (id)
);

CREATE TABLE assembly_to_computational_process_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES assembly_to_computational_process_association (id)
);

CREATE TABLE assembly_to_operational_activity_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES assembly_to_operational_activity_association (id)
);

CREATE TABLE assembly_to_operational_activity_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES assembly_to_operational_activity_association (id)
);

CREATE TABLE association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE behavioral_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE behavioral_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE behavioral_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE biological_sex_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biological_sex_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biological_sex_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE class_to_expression_site_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES class_to_expression_site_association (id)
);

CREATE TABLE class_to_expression_site_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES class_to_expression_site_association (id)
);

CREATE TABLE class_to_pathway_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES class_to_pathway_association (id)
);

CREATE TABLE class_to_pathway_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES class_to_pathway_association (id)
);

CREATE TABLE contributor_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE control_entity_assesses_named_thing_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES control_entity_assesses_named_thing_association (id)
);

CREATE TABLE control_entity_assesses_named_thing_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_entity_assesses_named_thing_association (id)
);

CREATE TABLE control_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES control_exposure (id)
);

CREATE TABLE control_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES control_exposure (id)
);

CREATE TABLE control_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_exposure (id)
);

CREATE TABLE control_mixture_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES control_mixture (id)
);

CREATE TABLE control_mixture_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES control_mixture (id)
);

CREATE TABLE control_mixture_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_mixture (id)
);

CREATE TABLE control_mixture_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(1), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES control_mixture (id)
);

CREATE TABLE control_role_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES control_role (id)
);

CREATE TABLE control_role_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES control_role (id)
);

CREATE TABLE control_role_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_role (id)
);

CREATE TABLE control_to_control_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES control_to_control_association (id)
);

CREATE TABLE control_to_control_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_to_control_association (id)
);

CREATE TABLE control_to_fault_or_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES control_to_fault_or_observable_feature_association (id)
);

CREATE TABLE control_to_fault_or_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_to_fault_or_observable_feature_association (id)
);

CREATE TABLE control_to_pathway_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES control_to_pathway_association (id)
);

CREATE TABLE control_to_pathway_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES control_to_pathway_association (id)
);

CREATE TABLE dataset_version_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE dataset_version_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE dataset_version_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE device_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE device_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE device_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE empirical_attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_attribute (id)
);

CREATE TABLE empirical_attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_attribute (id)
);

CREATE TABLE empirical_attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_attribute (id)
);

CREATE TABLE empirical_course_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_course (id)
);

CREATE TABLE empirical_course_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_course (id)
);

CREATE TABLE empirical_course_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_course (id)
);

CREATE TABLE empirical_measurement_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_measurement (id)
);

CREATE TABLE empirical_measurement_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_measurement (id)
);

CREATE TABLE empirical_measurement_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_measurement (id)
);

CREATE TABLE empirical_modifier_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES empirical_modifier (id)
);

CREATE TABLE empirical_modifier_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES empirical_modifier (id)
);

CREATE TABLE empirical_modifier_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES empirical_modifier (id)
);

CREATE TABLE entity_to_fault_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_fault_association (id)
);

CREATE TABLE entity_to_fault_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_fault_association (id)
);

CREATE TABLE entity_to_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_observable_feature_association (id)
);

CREATE TABLE entity_to_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_observable_feature_association (id)
);

CREATE TABLE environmental_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE exposure_event_to_outcome_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE fault_or_observable_feature_to_location_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature_to_location_association (id)
);

CREATE TABLE fault_or_observable_feature_to_location_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fault_or_observable_feature_to_location_association (id)
);

CREATE TABLE fault_to_exposure_event_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES fault_to_exposure_event_association (id)
);

CREATE TABLE fault_to_exposure_event_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fault_to_exposure_event_association (id)
);

CREATE TABLE faulty_deployment_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES faulty_deployment_exposure (id)
);

CREATE TABLE faulty_deployment_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES faulty_deployment_exposure (id)
);

CREATE TABLE faulty_deployment_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES faulty_deployment_exposure (id)
);

CREATE TABLE faulty_process_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process_exposure (id)
);

CREATE TABLE faulty_process_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process_exposure (id)
);

CREATE TABLE faulty_process_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES faulty_process_exposure (id)
);

CREATE TABLE functional_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE geographic_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE geographic_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE geographic_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE homogeneity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES homogeneity (id)
);

CREATE TABLE homogeneity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES homogeneity (id)
);

CREATE TABLE homogeneity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES homogeneity (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE observable_quality_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES observable_quality (id)
);

CREATE TABLE observable_quality_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES observable_quality (id)
);

CREATE TABLE observable_quality_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES observable_quality (id)
);

CREATE TABLE onset_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE onset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE onset_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE operational_activity_to_pathway_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES operational_activity_to_pathway_association (id)
);

CREATE TABLE operational_activity_to_pathway_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES operational_activity_to_pathway_association (id)
);

CREATE TABLE operational_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES operational_entity (id)
);

CREATE TABLE operational_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES operational_entity (id)
);

CREATE TABLE operational_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES operational_entity (id)
);

CREATE TABLE population_to_population_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE procedure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE procedure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE procedure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE redundancy_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES redundancy_entity (id)
);

CREATE TABLE redundancy_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES redundancy_entity (id)
);

CREATE TABLE redundancy_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES redundancy_entity (id)
);

CREATE TABLE replica_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES replica (id)
);

CREATE TABLE replica_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES replica (id)
);

CREATE TABLE replica_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES replica (id)
);

CREATE TABLE severity_value_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE severity_value_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE severity_value_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE socioeconomic_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE socioeconomic_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE socioeconomic_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE system_attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES system_attribute (id)
);

CREATE TABLE system_attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES system_attribute (id)
);

CREATE TABLE system_attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES system_attribute (id)
);

CREATE TABLE system_taxon_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES system_taxon (id)
);

CREATE TABLE system_taxon_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES system_taxon (id)
);

CREATE TABLE system_taxon_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES system_taxon (id)
);

CREATE TABLE system_to_system_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES system_to_system_association (id)
);

CREATE TABLE system_to_system_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES system_to_system_association (id)
);

CREATE TABLE workload_background_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES workload_background_exposure (id)
);

CREATE TABLE workload_background_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES workload_background_exposure (id)
);

CREATE TABLE workload_background_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES workload_background_exposure (id)
);

CREATE TABLE service_type_to_class_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES service_type (id), 
	FOREIGN KEY(object) REFERENCES class (id)
);

CREATE TABLE service_type_to_observable_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES service_type (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE service_type_to_service_type_part_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES information_resource (id), 
	FOREIGN KEY(subject) REFERENCES service_type (id), 
	FOREIGN KEY(object) REFERENCES service_type (id)
);

CREATE TABLE administrative_operation_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation (id)
);

CREATE TABLE administrative_operation_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation (id)
);

CREATE TABLE administrative_operation_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation (id)
);

CREATE TABLE administrative_operation_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(1), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES administrative_operation (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE case_to_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES case_to_observable_feature_association (id)
);

CREATE TABLE case_to_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES case_to_observable_feature_association (id)
);

CREATE TABLE class_to_fault_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES class_to_fault_association (id)
);

CREATE TABLE class_to_fault_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES class_to_fault_association (id)
);

CREATE TABLE class_to_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES class_to_observable_feature_association (id)
);

CREATE TABLE class_to_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES class_to_observable_feature_association (id)
);

CREATE TABLE complex_operational_mixture_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES complex_operational_mixture (id)
);

CREATE TABLE complex_operational_mixture_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES complex_operational_mixture (id)
);

CREATE TABLE complex_operational_mixture_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES complex_operational_mixture (id)
);

CREATE TABLE complex_operational_mixture_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(1), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES complex_operational_mixture (id)
);

CREATE TABLE controllable_class_to_fault_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES controllable_class_to_fault_association (id)
);

CREATE TABLE controllable_class_to_fault_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES controllable_class_to_fault_association (id)
);

CREATE TABLE controllable_class_to_fault_association_has_evidence (
	backref_id TEXT, 
	has_evidence VARCHAR(1), 
	PRIMARY KEY (backref_id, has_evidence), 
	FOREIGN KEY(backref_id) REFERENCES controllable_class_to_fault_association (id)
);

CREATE TABLE exposure_event_to_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_observable_feature_association (id)
);

CREATE TABLE exposure_event_to_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_observable_feature_association (id)
);

CREATE TABLE fault_to_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES fault_to_observable_feature_association (id)
);

CREATE TABLE fault_to_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fault_to_observable_feature_association (id)
);

CREATE TABLE operational_mixture_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES operational_mixture (id)
);

CREATE TABLE operational_mixture_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES operational_mixture (id)
);

CREATE TABLE operational_mixture_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES operational_mixture (id)
);

CREATE TABLE operational_mixture_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(1), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES operational_mixture (id)
);

CREATE TABLE processed_material_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(1), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE reaction_to_catalyst_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_participant_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE service_type_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES service_type (id)
);

CREATE TABLE service_type_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES service_type (id)
);

CREATE TABLE service_type_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES service_type (id)
);

CREATE TABLE service_type_to_fault_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_fault_association (id)
);

CREATE TABLE service_type_to_fault_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_fault_association (id)
);

CREATE TABLE socioeconomic_attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE socioeconomic_attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE socioeconomic_attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE taxon_to_taxon_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE service_type_to_class_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_class_association (id)
);

CREATE TABLE service_type_to_class_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_class_association (id)
);

CREATE TABLE service_type_to_observable_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_observable_feature_association (id)
);

CREATE TABLE service_type_to_observable_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_observable_feature_association (id)
);

CREATE TABLE service_type_to_service_type_part_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_service_type_part_association (id)
);

CREATE TABLE service_type_to_service_type_part_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES service_type_to_service_type_part_association (id)
);
