# Introduction

The ISO 26262 series of standards is the adaptation of IEC 61508 series of standards to address the sector specific needs of electrical and/or electronic (E/E) systems within road vehicles. This adaptation applies to all activities during the safety lifecycle of safety-related systems comprised of electrical, electronic and software components.

Safety is one of the key issues in the development of road vehicles. Development and integration of automotive functionalities strengthen the need for functional safety and the need to provide evidence that functional safety objectives are satisfied.

With the trend of increasing technological complexity, software content and mechatronic implementation, there are increasing risks from systematic failures and random hardware failures, these being considered within the scope of functional safety. ISO 26262 series of standards includes guidance to mitigate these risks by providing appropriate requirements and processes.

To achieve functional safety, the ISO 26262 series of standards:

- a) provides a reference for the automotive safety lifecycle and supports the tailoring of the activities to be performed during the lifecycle phases, i.e., development, production, operation, service and decommissioning;
- b) provides an automotive-specific risk-based approach to determine integrity levels [Automotive Safety Integrity Levels (ASILs)];
- c) uses ASILs to specify which of the requirements of ISO 26262 are applicable to avoid unreasonable residual risk;
- d) provides requirements for functional safety management, design, implementation, verification, validation and confirmation measures; and
- e) provides requirements for relations between customers and suppliers.

The ISO 26262 series of standards is concerned with functional safety of E/E systems that is achieved through safety measures including safety mechanisms. It also provides a framework within which safety-related systems based on other technologies (e.g. mechanical, hydraulic and pneumatic) can be considered.

The achievement of functional safety is influenced by the development process (including such activities as requirements specification, design, implementation, integration, verification, validation and configuration), the production and service processes and the management processes.

Safety is intertwined with common function-oriented and quality-oriented activities and work products. The ISO 26262 series of standards addresses the safety-related aspects of these activities and work products.

Figure 1 shows the overall structure of the ISO 26262 series of standards. The ISO 26262 series of standards is based upon a V-model as a reference process model for the different phases of product development. Within the figure:

- — the shaded “V”s represent the interconnection among ISO 26262-3, ISO 26262-4, ISO 26262-5, ISO 26262-6 and ISO 26262-7;
- — for motorcycles:
- - — ISO 26262-12:2018, Clause 8 supports ISO 26262-3;
- — ISO 26262-12:2018, Clauses 9 and 10 support ISO 26262-4;

— the specific clauses are indicated in the following manner: “m-n”, where “m” represents the number of the particular part and “n” indicates the number of the clause within that part.

Figure 1 — Overview of ISO 26262

# 1 Scope

This document is intended to be applied to safety-related systems that include one or more electrical and/or electronic (E/E) systems and that are installed in series production road vehicles, excluding mopeds. This document does not address unique E/E systems in special vehicles such as E/E systems designed for drivers with disabilities.

NOTE Other dedicated application-specific safety standards exist and can complement the ISO 26262 series of standards or vice versa.

Systems and their components released for production, or systems and their components already under development prior to the publication date of this document, are exempted from the scope of this edition. This document addresses alterations to existing systems and their components released for production prior to the publication of this document by tailoring the safety lifecycle depending on the alteration. This document addresses integration of existing systems not developed according to this document and systems developed according to this document by tailoring the safety lifecycle.

This document addresses possible hazards caused by malfunctioning behaviour of safety-related E/E systems, including interaction of these systems. It does not address hazards related to electric shock, fire, smoke, heat, radiation, toxicity, flammability, reactivity, corrosion, release of energy and similar hazards, unless directly caused by malfunctioning behaviour of safety-related E/E systems.

This document describes a framework for functional safety to assist the development of safety-related E/E systems. This framework is intended to be used to integrate functional safety activities into a company-specific development framework. Some requirements have a clear technical focus to implement functional safety into a product; others address the development process and can therefore be seen as process requirements in order to demonstrate the capability of an organization with respect to functional safety.

This document does not address the nominal performance of E/E systems.

This document specifies the requirements for supporting processes, including the following:

- interfaces within distributed developments;
- overall management of safety requirements;
- configuration management;
- change management;
- verification;
- documentation management;
- confidence in the use of software tools;
- qualification of software components;
- evaluation of hardware elements;
- proven in use argument;
  — interfacing an application that is out of scope of ISO 26262; and
  — integration of safety-related systems not developed according to ISO 26262.

A provides an overview on objectives, prerequisites and work products of this document.

# 2 Normative references

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

- ISO 26262-1, Road vehicles — Functional safety — Part 1: Vocabulary
- ISO 26262-2:2018, Road vehicles — Functional safety — Part 2: Management of functional safety
- ISO 26262-3:2018, Road vehicles — Functional safety — Part 3: Concept phase
- ISO 26262-4:2018, Road vehicles — Functional safety — Part 4: Product development at the system level
- ISO 26262-5:2018, Road vehicles — Functional safety — Part 5: Product development at the hardware level
- ISO 26262-6:2018, Road vehicles — Functional safety — Part 6: Product development at the software level
- ISO 26262-7:2018, Road vehicles — Functional safety — Part 7: Production, operation, service and decommissioning
- ISO 26262-9:2018, Road vehicles — Functional safety — Part 9: Automotive Safety Integrity Level (ASIL)-oriented and safety-oriented analyses

# 3 Terms and definitions

For the purposes of this document, the terms, definitions and abbreviated terms given in ISO 26262-1 apply.

ISO and IEC maintain terminological databases for use in standardization at the following addresses:

- IEC Electropedia: available at http://www.electropedia.org/
- ISO Online browsing platform: available at https://www.iso.org/obp

# 4 Requirements for compliance

# 4.1 Purpose

This clause describes how:

- a) to achieve compliance with the ISO 26262 series of standards;
- b) to interpret the tables used in the ISO 26262 series of standards; and
- c) to interpret the applicability of each clause, depending on the relevant ASIL(s).

# 4.2 General requirements

When claiming compliance with the ISO 26262 series of standards, each requirement shall be met, unless one of the following applies:

- a) tailoring of the safety activities in accordance with ISO 26262-2 has been performed that shows that the requirement does not apply; or

ISO 26262-8:2018(E)

b) a rationale is available that the non-compliance is acceptable and the rationale has been evaluated in accordance with ISO 26262-2.

Informative content, including notes and examples, is only for guidance in understanding, or for clarification of the associated requirement, and shall not be interpreted as a requirement itself or as complete or exhaustive.

The results of safety activities are given as work products. “Prerequisites” are information which shall be available as work products of a previous phase. Given that certain requirements of a clause are ASIL-dependent or may be tailored, certain work products may not be needed as prerequisites.

“Further supporting information” is information that can be considered, but which in some cases is not required by the ISO 26262 series of standards as a work product of a previous phase and which may be made available by external sources that are different from the persons or organizations responsible for the functional safety activities.

# 4.3 Interpretations of tables

Tables are normative or informative depending on their context. The different methods listed in a table contribute to the level of confidence in achieving compliance with the corresponding requirement. Each method in a table is either:

- a) a consecutive entry (marked by a sequence number in the leftmost column, e.g. 1, 2, 3), or
- b) an alternative entry (marked by a number followed by a letter in the leftmost column, e.g. 2a, 2b, 2c).

For consecutive entries, all listed highly recommended and recommended methods in accordance with the ASIL apply. It is allowed to substitute a highly recommended or recommended method by others not listed in the table, in this case, a rationale shall be given describing why these comply with the corresponding requirement. If a rationale can be given to comply with the corresponding requirement without choosing all entries, a further rationale for omitted methods is not necessary.

For alternative entries, an appropriate combination of methods shall be applied in accordance with the ASIL indicated, independent of whether they are listed in the table or not. If methods are listed with different degrees of recommendation for an ASIL, the methods with the higher recommendation should be preferred. A rationale shall be given that the selected combination of methods or even a selected single method complies with the corresponding requirement.

NOTE A rationale based on the methods listed in the table is sufficient. However, this does not imply a bias for or against methods not listed in the table.

For each method, the degree of recommendation to use the corresponding method depends on the ASIL and is categorized as follows:

- — “++” indicates that the method is highly recommended for the identified ASIL;
- — “+” indicates that the method is recommended for the identified ASIL; and
- — “o” indicates that the method has no recommendation for or against its usage for the identified ASIL.

# 4.4 ASIL-dependent requirements and recommendations

The requirements or recommendations of each sub-clause shall be met for ASIL A, B, C and D, if not stated otherwise. These requirements and recommendations refer to the ASIL of the safety goal.

If ASIL decomposition has been performed at an earlier stage of development, in accordance with ISO 26262-9:2018, Clause 5, the ASIL resulting from the decomposition shall be met.

If an ASIL is given in parentheses in the ISO 26262 series of standards, the corresponding sub-clause shall be considered as a recommendation rather than a requirement for this ASIL. This has no link with the parenthesis notation related to ASIL decomposition.

# 4.5 Adaptation for motorcycles

For items or elements of motorcycles for which requirements of ISO 26262-12 are applicable, the requirements of ISO 26262-12 supersede the corresponding requirements in this document. Requirements of ISO 26262-2 that are superseded by ISO 26262-12 are defined in Part 12.

# 4.6 Adaptation for trucks, buses, trailers and semi-trailers

Content that is intended to be unique for trucks, buses, trailers and semi-trailers (T&B) is indicated as such.

# 5 Interfaces within distributed developments

# 5.1 Objectives

The objectives of this clause are:

- a) to define the interactions and dependencies between customers and suppliers for development activities;
- b) to describe the allocation of responsibilities; and
- c) to identify the work products to be exchanged for distributed developments of an item and its elements.

# 5.2 General

The customer (e.g. vehicle manufacturer) and the suppliers for item or element developments jointly comply with the requirements specified in the ISO 26262 series of standards for distributed developments. Responsibilities are agreed between the customer and the suppliers for the concept, development, production, operation, service and decommissioning phases of the safety lifecycle. Subcontractor relationships are permitted. The customer has safety-related procedures concerning planning, execution and documentation for in-house item developments, therefore comparable procedures apply for co-operation with the supplier on distributed item developments. The same applies for item developments where the supplier has the full responsibility for functional safety.

NOTE 1 The Development Interface Agreement (DIA) aims to describe the roles and responsibilities between the customer and supplier. Consequently the safety planning by the customer and supplier is in line with the DIA.

NOTE 2 This clause is not relevant for the procurement which do not place any responsibility for safety on the supplier, including standard components and parts or development commissions.

NOTE 3 This note applies to T&B: this clause is not relevant for body builder equipment being integrated into base vehicles. Clause 15 applies when integrating body builder equipment developed according to ISO 26262 into a base vehicle which is in scope of another standard. Clause 16 applies when body builder equipment developed according to another standard is integrated into a base vehicle developed according to ISO 26262.

# 12 Qualification of software components

# 12.1 Objectives

The objective of the qualification of software components is to provide evidence for their suitability for re-use in items developed in compliance with the ISO 26262 series of standards.

# 12.2 General

The use of qualified software components avoids re-development of existing software components with identical functionalities or properties or enables the use of general purpose commercial off-the-shelf (COTS) software.

NOTE Software components are understood to include source code, models, pre-compiled code, or compiled and linked software.

3. Automotive SPICE® is an example of a suitable product available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by ISO of these products.

EXAMPLE

Software components addressed by this clause include:

- software libraries from third-party suppliers [commercial off-the-shelf (COTS) software];
- already existing SW components not developed according to ISO 26262;
- in-house components already in use in electronic control units.

# 12.3 Inputs to this clause

# 12.3.1 Prerequisites

The following information shall be available:

- organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1; and
- requirements of the software component (from an external source).

# 12.3.2 Further supporting information

The following information can be considered:

- design specification of the software component (from an external source); and
- results of previous verification measures of the software component (from an external source).

# 12.4 Requirements and recommendations

# 12.4.1 General

To be able to consider a software component as qualified, the following shall be available:

1. the specification of the software component in accordance with 12.4.2.1;
2. evidence that the software component complies with its requirements in accordance with 12.4.2.2, 12.4.2.3, and 12.4.2.4;
3. evidence that the software component is suitable for its intended use in accordance with 12.4.3;
4. evidence that the software development process for the component is based on an appropriate national or international standard (e.g. ISO/IEC/IEEE 12207); and
5. a plan for the qualification of the software component.

NOTE Some re-engineering activities can be performed in order to comply with this sub-clause in the case of previously developed software components.

# 12.4.2 Specification of software component qualification

# 12.4.2.1 The specification of the software component qualification shall include:

1. the unique identification of the software component;
2. the maximum target ASIL of any safety requirement which might be violated if the software component performs incorrectly;
3. the activities that shall be carried out to qualify the software component;
4. the requirements of the software component;

Requirements can include:

- functional requirements;
- already known safety requirements;
- accuracy of algorithm or numerical accuracy, where accuracy of algorithm considers procedural errors, which only provide approximate solutions and numerical accuracy considers rounding errors, resulting from computational inaccuracy, and truncation errors caused by the approximate representation of functions in the electronic control unit;
- behaviour in the case of failure;
- response time;
- resource usage;
- requirements on the runtime environment; and
- behaviour in an overload situation (robustness).

e) the requirements of the intended use of the software component;

f) the description of the configuration;

NOTE For software components that contain more than one software unit, the description of the configuration includes the unique identification and configuration of each software unit.

g) the description of required and provided interfaces and shared resources, if any;

h) the application manual, where appropriate;

i) the instructions for a correct software component integration;

NOTE This description includes configuration parameters of the development tools required to properly integrate and use the software component.

j) the reactions of the implemented functions under anomalous operating conditions; and

EXAMPLE Reaction to re-entrant calling of a non-re-entrant software function.

k) a description of known anomalies with corresponding workaround measures.

# 12.4.2.2

To provide evidence that a software component complies with its requirements the verification of this software component shall:

- show a requirement coverage in accordance with ISO 26262-6:2018, Clause 9;
- NOTE This verification is primarily based on requirements-based tests. The results of requirements-based tests of the software component executed during its development or during previous integration tests can be used.

EXAMPLE Application of a dedicated qualification test suite, analysis of all the tests already executed during the implementation and any integration of the software component.

cover both normal operating conditions and behaviour in the case of failure; and

- display no known errors that may lead to a violation of safety requirements allocated to this software component.

# 12.4.2.3

This requirement applies to ASIL D, in accordance with 4.4: the structural coverage shall be measured in accordance with ISO 26262-6:2018, Clause 9, to evaluate the completeness of the test cases.

# 12.4.2.4

The verification in accordance with 12.4.2.2, shall only be valid for an unchanged implementation of the software component.

# 12.4.2.5

The qualification of a software component shall be documented including the following information:

- a) the unique identification of the software component;
- b) the unique configuration of the software component;
- c) the person or organization who carried out the qualification;
- d) the environment used for qualification;
- e) the results of the verification measures applied to qualify the software component; and
- f) the maximum ASIL of the safety requirements allocated to the software component.

# 12.4.3 Verification of qualification of a software component

The results of qualification of a software component together with the validity of these results regarding the intended use of the software component shall be verified in accordance with Clause 9.

# 12.5 Work products

# 12.5.1

Software component documentation resulting from requirement 12.4.2.1.

# 12.5.2

Software component qualification report resulting from requirements 12.4.2.2 to 12.4.2.5.

# 12.5.3

Software component qualification verification report resulting from requirement 12.4.3.

# 13 Evaluation of hardware elements

# 13.1 Objectives

The objective of this clause is to ensure that the functional behaviour is adequate to meet the allocated safety requirements and therefore the risk of a violation of a safety goal or of a safety requirement, due to a systematic fault of the hardware element, is sufficiently low. Suitability for use based on random fault management is established by the integrator of the evaluated hardware element, at the next highest level of design integration.

NOTE 1 Meeting the requirements of the safety concept includes providing information on failure modes and failure mode distribution of the hardware element, suitable to conduct hardware failure analysis.

NOTE 2 It is not the objective of this clause to ensure the suitability of the hardware element concerning its robustness in its intended environmental conditions or its reliability. This is addressed for every hardware element within ISO 26262-5:2018, Clause 10.

In this clause, the use of the term “hardware element” refers either to COTS hardware components or parts, or to custom hardware components or parts, that:

- — are not originally developed or designed according to the ISO 26262 series of standards; and
- — are considered to be safety-related within the context of the ISO 26262 compliant item or element into which they are to be integrated.

More precisely, the evaluation of hardware elements is an alternative means of compliance with ISO 26262-5. The hardware elements eligible for evaluation can either be specific to an application.

# 13.2 General

The following goals are achieved by the evaluation of hardware elements:

- a) provide evidence that the hardware possesses an adequate functional performance and therefore is suitable to provide its intended function as required by the hardware design;
- b) identification of new or confirmation of known failure modes and models (including the quantification of their distribution) by using appropriate tests (such as over limit test, accelerated test, etc.) or analyses;
- c) identification of new or confirmation of known limits of use for hardware elements; and
- d) provide an argument that the risk of a violation of a safety goal or the risk of a violation of a safety requirement due to systematic faults is sufficiently low.

The evaluation of hardware elements is done in the context of a specific application. Within the evaluation of hardware elements the hardware element under consideration is classified either as class I, class II or class III element depending on its properties. These classes reflect the difficulty of the verification of the safety-related functionality and the role of the hardware element within the safety concept.

Depending on its class, different requirements to evaluate the hardware element are given. As a first step the relevant requirements for the hardware element are specified and its safety related failure modes are identified.

For the evaluation of class I elements it is sufficient to test the hardware element into which the evaluated hardware elements are integrated according to ISO 26262-5:2018, Clause 10. The evaluation of class II elements can be done with a combination of tests and analyses. For the evaluation of class III elements, in addition to the evaluation activities necessary for a class II element, an argument is added showing that the risk of a safety goal violation or the risk of a safety requirement violation is sufficiently low.

# 13.3 Inputs to this clause

# 13.3.1 Prerequisites

The following information shall be available:

- — organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1;
- — the safety requirements related to the considered hardware element;
- — criteria for design verification (analysis and tests) in accordance with ISO 26262-5:2018, Clause 6; and
- — the manufacturer's hardware element specification, or, if unavailable, the assumptions on hardware element specification (from an external source).

# 13.3.2 Further supporting information

The following information can be considered:

- — further supporting information for the phases of the safety lifecycle where the evaluation of hardware elements is applied.

# 13.4 Requirements and recommendations

# 13.4.1 General

# 13.4.1.1 Classification of the evaluated hardware element

The hardware element shall be classified as one of the following classes:

a) Class I if:

- the element has at the maximum a few states which can be fully characterized, tested and analysed from a safety perspective;
- safety related failure modes can be identified and evaluated without knowledge about details of the implementation and the production process of the element; and
- the element has no internal safety mechanisms which are relevant for the safety concept to control or detect internal failures.

NOTE This does not include safety mechanisms that monitor properties outside of the element.

EXAMPLE Resistor, capacitor, transistor, diode, quartz, resonator.

b) Class II if:

- the element has e.g. few operating modes, small value ranges, few parameters and can be analysed from safety perspective without knowing implementation details;
- available documentation allows valid assumptions supporting evaluation of systematic faults by testing and analysis without knowledge about details of the implementation and the production process of the element; and

EXAMPLE Datasheets, user manuals, application notes.

- the element has no internal safety mechanisms which are relevant for the safety concept to control or detect internal failures.

NOTE This does not include safety mechanisms that monitor properties outside of the element.

EXAMPLE Fuel pressure sensor, temperature sensor, stand-alone Analog Digital Converter (ADC) without internal safety mechanisms relevant for the safety concept.

c) Class III if:

- the element has e.g. many operating modes, wide value ranges or many parameters which are impossible to analyse without knowing implementation details,
- sources for systematic faults can only be understood and analysed by knowledge about detailed implementation, the development process and/or the production process, or
- the element has internal safety mechanisms which are relevant for the safety concept to control or detect internal failures.

EXAMPLE Microprocessor, microcontroller, Digital Signal Processor (DSP).

# 13.4.1.2 The requirements for the hardware element resulting from the allocated safety requirements

and the safety concept shall be specified.

NOTE For class I elements this usually coincides with the specification of the hardware element, e.g. nominal value and tolerances for a resistor.

# 13.4.1.3

The failure modes or faults of the hardware element and their distribution concerning random hardware faults shall be identified.

# 13.4.1.4

The safety related failure modes or faults of the hardware element shall be identified. The analysis shall provide evidence that the requirements resulting from ISO 26262-5:2018, 7.4.3, Clauses 8 and 9 are met.

# 13.4.2 Evaluation of class I hardware elements

Due to the simplicity of the functionality of a class I element, it does not need to be evaluated by itself; the hardware element into which it is integrated shall be developed in compliance with ISO 26262.

# 13.4.3 Evaluation of class II hardware elements

# 13.4.3.1 Methods for evaluation

The evaluation of the class II hardware element shall be carried out using an appropriate selection of analysis and testing.

# 13.4.3.2 Evaluation plan

An evaluation plan shall be developed and shall describe:

- a unique identification and version of the hardware element;
- a specification of the environment in which the hardware element is intended to be used;
- the evaluation strategy and the rationale;

NOTE The strategy includes: analysis, necessary tests and step by step description.

- the necessary tools and equipment according to the strategy;
- the party responsible for carrying out the evaluation; and
- the pass and fail criteria for the evaluation of a hardware element.

# 13.4.3.3 Evaluation argument

# 13.4.3.3.1

A comprehensive argument that the functional performance of the hardware element complies with its specification and it is adequate for its intended use, according to the hardware design, shall be made available.

NOTE The required performances encompass behaviour when it is subjected to the established normal environmental conditions and to the environmental conditions in combination with an assumed failure initiating event.

# 13.4.3.3.2

The comprehensive argument of 13.4.3.3.1 shall be based on a combination of the following types of information:

- analytical methods and assumptions used;
- data from operational experience; and
- existing testing results.

# 13.4.3.3.3

A rationale for each assumption, including extrapolations, shall be given.

# 13.4.3.4 Evaluation by analyses

# 13.4.3.4.1

The result of the analysis shall be provided in a form that is comprehensive and can be verified by persons who are qualified in the relevant engineering or scientific disciplines.

NOTE Analytical methods that can be used include design verification methods, e.g. extrapolations, mathematical models, damage analysis or similar methods, and process gap analysis in order to show sufficient evidence for systematic failure avoidance will be available.

# 13.4.3.4.2

The analysis shall consider all the environmental conditions to which the hardware element is exposed, the limits of these conditions and other additional stresses related to operation (e.g. expected switch cycles, charging and discharging, long turn-off times).

# 13.4.3.5 Evaluation by testing

# 13.4.3.5.1

A test plan shall be developed which contains the following information:

- a) a description of the functions of the hardware element;
- b) allocated safety requirements;
- c) the specification and sequence of tests to be conducted;
- d) the traceability between tests and safety requirements;
- e) the requirements for assembly and connections;
- f) the operating and environmental conditions to be simulated;
- g) number of elements tested;
- h) pass and fail criteria;
- i) environmental parameters to be measured; and
- j) requirements for the testing equipment, including accuracy.

# 13.4.3.5.2

The test to verify robustness of the hardware element under evaluation against external stresses shall be done in accordance with ISO 26262-5:2018, 10.4.6.

EXAMPLE This specification can be based on the ISO 16750 series of standards or equivalent company standards.

# 13.4.3.5.3

The test shall be conducted as planned and the resulting test data shall be made available.

# 13.4.3.5.4

The integration into the ISO 26262 compliant element shall comply with ISO 26262-5:2018, Clause 10 or ISO 26262-4:2018, Clause 7.

# 13.4.3.6 Evaluation report

# 13.4.3.6.1

The evaluation report shall state whether the hardware element has passed or failed the evaluation, based on the performed analyses and testing, with respect to the safety requirements specified and allocated to it, including its operating range and conditions.

NOTE The evaluation report can consist of a set of documents that includes reports on findings and notes on interpretation.

# 13.4.3.6.2

The evaluation report shall be verified in accordance with Clause 9.

# 13.4.4 Evaluation of class III hardware elements

# 13.4.4.1

Class III hardware elements should be developed in compliance with ISO 26262.

NOTE This means that the “evaluation of class III elements” is not the preferred approach and therefore the next version of the hardware element is planned to be developed in compliance with ISO 26262.

# 13.4.4.2

For the evaluation of the class III hardware elements the requirements stated in 13.4.3 shall be met.

# 13.4.4.3

Additional measures shall be provided to argue that the risk of a safety goal violation or the risk of a safety requirement violation due to systematic faults is sufficiently low.

NOTE 1 Depending on the combination of arguments provided, the result of the hardware evaluation shows that using the class III element in the context of the given application is safe. However the argument is not valid for all applications.

NOTE 2 Measures can include but are not limited to:

- a) verifiability of the safety related functionality;
- b) field experience/“well-trusted component”; NOTE Field experience can be used as a partial supporting argument for hardware evaluation. For a full proven-in-use argument, ISO 26262-8:2018, Clause 14 is followed instead of this clause.
- c) supervision by an independent diverse element with the capability to detect the safety related failure modes; NOTE A Dependent Failure Analysis compliant with ISO 26262-9:2018, Clause 7, shows the independence.
- d) development compliant with a different safety standard with a comparable integrity level.

# 13.5 Work products

# 13.5.1

Hardware element evaluation plan resulting from requirement 13.4.3.2.

# 13.5.2

Hardware element test plan if applicable, resulting from requirement 13.4.3.5.1.

# 13.5.3

Hardware element evaluation report for hardware elements resulting from requirements 13.4.1.1, 13.4.3.6 and 13.4.4.3, if applicable.

# 14 Proven in use argument

# 14.1 Objectives

The objective of this clause is to provide guidance for a proven in use argument. A proven in use argument is an alternate means of compliance with the ISO 26262 series of standards that may be used in the case of reuse of existing items or elements when field data is available.

# 14.2 General

A proven in use argument can be applied to any type of product whose definition and conditions of use are identical to or have a very high degree of commonality with a product that is already released and in operation. It can also be applied to any work product related to such products.

NOTE 1 Proven in use argument is not inter-changeability: one product, with alternate design or implementation, that is intended to replace a proven in use product cannot be considered to be proven in use because it fulfils the original functional requirements, unless this product meets the criteria specified in this clause.

An item or an element, such as system, function, hardware or whole software product, can be a candidate for a proven in use argument. A candidate can also refer to a work product such as a technical safety concept.

The motivation for using the argument for proven in use includes:

- a) an automotive application in commercial use intended to be partly or completely carried over to another target, or
- b) an Electronic Control Unit (ECU) in operation intended to implement an additional function, or
- c) a candidate being in the field prior to the release of the ISO 26262 series of standards, or
- d) a candidate being used in other safety-related industries, or
- e) a candidate being a widely used COTS product not necessarily intended for automotive applications.

The proven in use argument is substantiated by appropriate documentation on the candidate, configuration management and change management records, and field data regarding safety-related incidents.

Once a candidate has been defined (see 14.4.3) with the expected proven in use credit (see 14.4.2), two important criteria need to be considered when preparing a proven in use argument:

- — the relevance of field data during the previous evaluation period of the candidate (see 14.4.5); and
- — the changes, if any, that could have impacted the candidate since its previous evaluation period (see 14.4.4).

NOTE 2 With regard to the relevance of field data, the proven in use argument is intended to address systematic and random failures of the candidate; it does not address failures related to ageing of the candidate.

Using proven in use items or elements does not exempt those items or elements from the following project-dependent safety management activities:

- — the proven in use credit is described in the safety plan; and
- — the data and work products resulting from the proven in use argument are part of the safety case and subject to confirmation measures.

# 14.3 Inputs to this clause

# 14.3.1 Prerequisites

The following information shall be available:

- — regarding the intended use of a candidate:

— foreseeable operational situation and intended operating modes and interfaces;

— regarding the previous use of a candidate:

— field data from the service period (from an external source).

# 14.3.2 Further supporting information

The following information can be considered regarding the previous use of a candidate:

— safety case in accordance with ISO 26262-2:2018, 6.5.4.

NOTE For a candidate not developed in accordance with the ISO 26262 series of standards (e.g. COTS products, candidates developed under a safety standard other than ISO 26262, such as IEC 61508 or RTCA DO-178C), some work products of the safety case may not be available, in which case they are substituted by available data resulting from the development of the candidate.

# 14.4 Requirements and recommendations

# 14.4.1 General

The following sub-clauses refer to the ASILs applicable to the future use of the candidate.

# 14.4.2 Proven in use credit

# 14.4.2.1

A proven in use credit shall be used only when the candidate complies with 14.4.2 to 14.4.5.

# 14.4.2.2

The proven in use credit resulting from a proven in use argument shall be planned in accordance with ISO 26262-2:2018, 6.4.5.

# 14.4.2.3

The proven in use credit shall be limited to the safety lifecycle sub-phases and activities covered by the proven in use argument of the candidate.

# 14.4.2.4

Integration measures of proven in use elements in an item or element shall be carried out at the appropriate level in accordance with ISO 26262-4:2018, Clause 8.

EXAMPLE The hardware of an ECU has a satisfactory field history and is intended to be 100 % carried over to a new application. The proven in use credit can be applied to the sub-phases and activities of development of this hardware element. Similarly, if the software is a 100 % carryover with a satisfactory service history, then the proven in use credit can also be applied to the software sub-phases and activities.

# 14.4.2.5

Safety validation of an item which embeds proven in use elements shall be carried out in accordance with ISO 26262-4:2018, Clause 9.

# 14.4.2.6

The confirmation measures of an item that embeds proven in use elements shall consider the proven in use arguments and related data in accordance with ISO 26262-2:2018, 6.4.9 and 6.4.10.

# 14.4.2.7

Any modification to a proven in use item or element shall comply with 14.4.4 for the corresponding proven in use credit to be maintained.

NOTE This clause applies to any type of modification including those initiated as a result of a safety-related incident.

# 14.4.3 Minimum information on candidate

A description of the candidate and its previous use shall be available, and includes:

- a) the identification and traceability of the candidate with a catalogue of internal elements or components, if any;
- b) the corresponding fit, form and function requirements that describe, if applicable, interface and environmental, physical and dimensional, functional and performance characteristics of the candidate; and
- c) the safety requirements of the candidate in the previous use and the corresponding ASILs, if available.

# 14.4.4 Analysis of modifications to the candidate

# 14.4.4.1 Proven in use candidates

Modifications to candidates and their environment shall be identified in accordance with 14.4.4.2 to 14.4.4.3.

NOTE 1 Modifications to candidates address design changes and implementation changes. Design changes can result from modification of requirements, functional enhancements or performance enhancement. Implementation changes do not affect specification or performance of the candidate but only its implementation features. Implementation changes can result from software corrections or use of new development or production tools.

NOTE 2 Changes to configuration data or calibration data are considered as modifications to the candidate when they impact its behaviour with regard to the violation of the safety goals.

NOTE 3 Changes to the environment of a candidate can result from use of this candidate in a new type of application with different safety goals or requirements, its installation in a new target environment (e.g. variant of vehicle, range of environmental conditions) or the upgrading of the components interacting with it or located in its vicinity.

# 14.4.4.2 Modifications to items introduced for a future application

Modifications to items and their environment introduced for the purpose of a future application shall comply with ISO 26262-2:2018, 6.4.3.

# 14.4.4.3 Modifications to elements introduced for a future application

Modifications to elements and their environment introduced for the purpose of a future application within a different item shall comply with ISO 26262-2:2018, 6.4.4.

# 14.4.4.4 Modifications to candidate independent of future application

Modifications to a candidate introduced after its evaluation period, independent of future applications, shall provide evidence that the proven in use status remains valid.

# 14.4.5 Analysis of field data

# 14.4.5.1 Configuration management and change management

Evidence shall be provided that the candidate has been kept under configuration management and change management during and after its evaluation period so that the current status of the candidate can be established.

# 14.4.5.2 Target values for proven in use

NOTE When any ASIL is not yet assigned to the candidate, ASIL D target is selected conservatively.

# 14.4.5.2.1

The rationale for the calculation of the evaluation period of the candidate shall be available.

# 14.4.5.2.2

The evaluation period of the candidate shall result from the addition of the observation period of all the specimens taken in reference in accordance with 14.4.5.2.3.

# 14.4.5.2.3

The observation period of each specimen with the same specification and realization as the candidate and running in a vehicle shall exceed the average yearly vehicle operating time before being considered in the analysis of the evaluation period of the candidate.

# 14.4.5.2.4

For a proven in use status to be obtained by the candidate, its evaluation period shall demonstrate compliance with each safety goal that can be violated by the candidate in accordance with Table 6 with a single-sided lower confidence level of 70 % (using a chi-square distribution).

NOTE 1 For the purpose of the proven in use argument, an observable incident means a failure that is reported to the manufacturer and caused by the candidate with the potential to lead to the violation of a safety goal.

**Table 6 — Limits for observable incident rate**
|ASIL|Observable incident rate|
|---|---|
|D|<10−9/h|
|C|<10−8/h|
|B|<10−8/h|
|A|<10−7/h|

NOTE 2 The character and rate of observable incidents are interpreted when analysing the potential violation of the safety goals in the field.

NOTE 3 Table 7 gives an example of the required minimum service period without observable incident which is necessary to achieve 70 % confidence.

**Table 7 — Targets for minimum evaluation period of candidate**
|ASIL|Minimum evaluation period without observable incident|
|---|---|
|D|1,2 × 109 h|
|C|1,2 × 108 h|
|B|1,2 × 108 h|
|A|1,2 × 107 h|

NOTE 4 If observable incidents are found in the collected data of the specimens, the necessary minimum evaluation period, tservice, can be adjusted as follows:

tservice = MTTF × (χCL;2 f + 2)2t2

where

- CL is the confidence level as an absolute value (e.g. 0,7 for 70 %);
- tMTTF is the mean time to failure (1/failure rate);
- f is the number of safety-related incidents;
- (χα, ν) is the chi-squared distribution with error probability α and ν degrees of freedom.

# 14.4.5.2.5

The application of the proven in use credit may be anticipated provisionally, before a proven in use status is obtained (in accordance with 14.4.5.2.4). In this case, the evaluation period of the candidate shall demonstrate compliance with each safety goal that can be violated by the candidate in accordance with Table 8 with a single sided lower confidence level of 70 % (using a chi-square distribution).

**Table 8 — Limits for observable incident rate (interim period)**
|ASIL|Observable incident rate|
|---|---|
|D|<3 × 10−9/h|
|C|<3 × 10−8/h|
|B|<3 × 10−8/h|
|A|<3 × 10−7/h|

# 14.4.5.2.6

In the case of any observed incident in the field during the interim period described in 14.4.5.2.5, the following shall be complied with:

- to stop using Table 8 for the observable incident rate and to use alternatively
- to provide evidence that the root cause of the observed incident is fully identified and eliminated in accordance with the ISO 26262 series of standards, and to keep on counting the cumulated hours for the candidate, to reset the counter of cumulated hours for this specific root cause and to record this evidence in the safety case.

# 14.4.5.2.7

In the case of a candidate with a non-constant failure rate, additional measures shall be applied for the proven in use argument, for instance in the case of damage resulting from fatigue.

NOTE Those measures apply to candidates with failure rates significantly dependent on factors such as wear, ageing or operating hours regarding the lifetime of the item. They can include dedicated endurance tests, or a longer observation period.

# 14.4.5.3

Field problems

The problem reporting system shall ensure that any observed incident with potential safety impact caused by the candidate in the field, is recorded and retrievable during the period of operation of the candidate (see ISO 26262-2:2018, 7.4.2.3).

# 14.5

Work products

# 14.5.1

Description of candidate for proven in use argument resulting from requirement 14.4.3.

# 14.5.2

Proven in use analysis reports resulting from requirements 14.4.4 to 14.4.5.

# 15 Interfacing an application that is out of scope of ISO 26262

# 15.1 Objectives

This clause applies to T&B, where the objective is to achieve confidence that an application that is out of scope of ISO 26262 is not able to violate the safety goals of the base vehicle or item that has been developed in accordance with the ISO 26262 series of standards.

# 15.2 General

The application of this clause is intended for commercial vehicle business models where a company assembles or integrates a complete vehicle that is not in scope of ISO 26262 but to which another standard applies. The relationship between the application and item according to ISO 26262 is depicted in Figure 5.

Figure 5 — Item developed according to ISO 26262 used in scope of another standard

EXAMPLE 1

A body builder, as an integrator, assembles a complete vehicle by integrating a base vehicle developed according to the ISO 26262 series of standards with body builder equipment developed according to the Machinery Directive.

EXAMPLE 2

A manufacturer of agricultural equipment integrates a brake system developed according to the ISO 26262 series of standards into agricultural equipment developed according to standards for machinery for agriculture and forestry.

# 15.3 Inputs to this clause

# 15.3.1 Prerequisites

The following information shall be available:

- item definition in accordance with ISO 26262-3:2018, 5.5.1

# 15.3.2 Further supporting information

None.

# 15.4 Requirements and recommendations

# 15.4.1

The requirements in 15.4 shall be applied to T&B.

# 15.4.2

The base vehicle manufacturer or supplier of an item or element shall communicate information to the integrator identifying the modifiable systems and components and the permitted system safety limits/requirements of the modifications.

# 15.4.3

The base vehicle manufacturer or supplier of an item shall communicate the safety measures required to be applied by the integrator.

NOTE 1 It is assumed that the integrator has the necessary capability to realize the safety measures.

EXAMPLE 1

Criteria for the capability of an integrator can be:

- compliance with other safety standards,
- an appropriate safety culture, and
- an established quality management system.

NOTE 2 The base vehicle manufacturer or supplier of an item or element makes assumptions about intended integrator use cases together with the safety requirements. For exceptions, the integrator contacts the base vehicle manufacturer or supplier of the item or element for safety requirements.

EXAMPLE 2 A body builder contacts a base vehicle manufacturer to request PTO activation during driving. The body builder uses ISO 13849 and both agree on an ASIL to ISO 13849. The base vehicle manufacturer communicates the safety requirements (with ASIL) regarding the PTO request, the body builder complies with these requirements (with agreed Performance Level). The base vehicle manufacturer enables the requested PTO function for the body builder.

# 15.5 Work products

# 15.5.1 Base Vehicle Manufacturer or Supplier guideline resulting from requirements 15.4.2 and 15.4.3.

# 16 Integration of safety-related systems not developed according to ISO 26262

# 16.1 Objectives

This clause applies to T&B, where the objective is to achieve confidence that a system or component that is not developed according the ISO 26262 series of standards satisfies the required level of functional safety needed for the integration into an item developed according to the ISO 26262 series of standards.

# 16.2 General

The application of this clause is intended for commercial vehicle business models where a company which follows ISO 26262 integrates a system or component which is not developed according to the ISO 26262 series of standards, but which has been developed according to another standard. The relationship between the application and item according to the ISO 26262 series of standards is depicted in Figure 6.

Figure 6 — Integration of a system developed according to another standard

NOTE 1 Since this business model can demand higher effort and development costs for the integrator due to additional safety activities, a conventional ISO 26262 development is favoured.

NOTE 2 A business model for commercial vehicles could be series production with low quantities.

NOTE 3 Another standard could be the Machinery Directive including IEC 61508, ISO 13849 and ISO 25119. Company specific processes could also be used for the integration.

# 16.3 Inputs to this clause

# 16.3.1 Prerequisites

The following information shall be available:

- item definition in accordance with ISO 26262-3:2018, 5.5.1.

NOTE 1 The Item definition relates to the system or array of systems on the integrator side, that includes the system or component not developed according to ISO 26262.

NOTE 2 An integrator of such systems or components can be the base vehicle manufacturer.

# 16.3.2 Further supporting information

None.

# 16.4 Requirements and recommendations

# 16.4.1

The requirements in 16.4 shall be applied to T&B.

# 16.4.2

A rationale shall be given in the integrator safety case that justifies the application of this clause.

EXAMPLE The supplier follows the safety standard ISO 13849.

# 16.4.3

The integrator shall define the criteria to argue that the safety-related system that has been developed to another safety standard meets the required level of functional safety.

EXAMPLE 1 A mapping between ASIL and PL (Performance Level as used in ISO 13849).

NOTE The criteria address the design process, the product design, qualification measures and approval process.

EXAMPLE 2 Comparison of requirements regarding applied methods and requested failure rates of different safety standards.

# 16.4.4

The integrator and supplier shall agree on the relevant set of measures to verify that the criteria are met.

EXAMPLE A set of measures can be:

- availability of the specification for the system to be integrated;
- evidence that the system to be integrated complies with its requirements by test report;
- structured design analysis for systematic design faults by FMEA, FTA, application of established design pattern/configurations;
- evidence that the system to be integrated is suitable for its intended use;
- evidence that the product release for the component is based on an adequate approval process by PPAP (Production Part Approval Process);
- design verification/validation testing by highly accelerated life testing, environmental testing, testing beyond specification limits, robustness testing; and
- analysis of field data.

# 16.5 Work products

# 16.5.1

Safety rationale resulting from requirements 16.4.2 to 16.4.4.

# A (informative) Overview of and workflow of supporting processes

Table A.1 provides an overview on objectives, prerequisites and work products of the supporting processes.

| Clause | Objectives                                                                                                                                                                                                                                                                                                                                 | Prerequisites                                                                                                                                 | Work products                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5      | The objectives of this Clause are: a) to define the interactions and dependencies between customers and suppliers for development activities; b) to describe the allocation of responsibilities; and c) to identify the work products to be exchanged for distributed developments of an item and its elements.                            | See applicable prerequisites of the relevant phases of the safety lifecycle for which the distributed development is planned and carried out. | 5.5.1 Supplier selection report resulting from requirements 5.4.2.1 and 5.4.2.2. 5.5.2 Development interface agreement (DIA) resulting from requirements 5.4.3, 5.4.5.1 and 5.4.5.2. 5.5.3 Supplier's safety plan resulting from requirements 5.4.3 and 5.4.4. 5.5.4 Functional safety assessment report resulting from requirements 5.4.5.3 and 5.4.5.4. 5.5.5 Supply agreement resulting from requirements 5.4.6.1 to 5.4.6.4. |
| 6      | The objectives of this Clause are: a) to ensure the correct specification of safety requirements with respect to their attributes and characteristics; and b) to ensure consistent management of safety requirements throughout the entire safety lifecycle.                                                                               | Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1.                                   | None                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 7      | The objectives of this Clause are: a) to ensure that the work products, items, elements and the principles and general conditions of their creation, can be uniquely identified and reproduced in a controlled manner at any time; and b) to ensure that the relations and differences between earlier and current versions can be traced. | Safety plan in accordance with ISO 26262-2:2018, 6.5.3.                                                                                       | 7.5.1 Configuration management plan resulting from requirements 7.4.1 to 7.4.5.                                                                                                                                                                                                                                                                                                                                                  |

Table A.1 (continued)

| Clause | Objectives                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Prerequisites                                                                                                                                                                                                                                                     |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8      | The objective of change management is to analyse and control changes to safety-related work products, items and elements throughout the safety lifecycle.                                                                                                                                                                                                                                                                                                                                                                                      | Configuration management plan in accordance with 7.5.1. Safety plan in accordance with ISO 26262-2:2018, 6.5.3. Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1.                                       |
| 9      | The objective of verification is to ensure that the work products comply with their requirements.                                                                                                                                                                                                                                                                                                                                                                                                                                              | Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1. Applicable prerequisites of the relevant phases of the safety lifecycle in which verification is planned or carried out.                              |
| 10     | The objective is to develop a documentation management strategy for the entire safety lifecycle in order to facilitate an effective and repeatable documentation management process.                                                                                                                                                                                                                                                                                                                                                           | Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1. Safety plan in accordance with ISO 26262-2:2018, 6.5.3.                                                                                               |
| 11     | The objectives of this Clause are: a) to provide criteria to determine the required level of confidence in a software tool when applicable; and b) to provide means for the qualification of the software tool when applicable, in order to create evidence that the software tool is suitable to be used to support the activities or tasks required by the ISO 26262 series of standards (i.e. the user can rely on the correct functioning of a software tool for those activities or tasks required by the ISO 26262 series of standards). | Safety plan in accordance with ISO 26262-2:2018, 6.5.3. Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1. Applicable prerequisites of the phases of the safety lifecycle where a software tool is used. |

Work products

8.5.1 Change management plan resulting from requirements 8.4.1.
8.5.2 Change request resulting from requirements 8.4.2.
8.5.3 Impact analysis and change request plan resulting from requirements 8.4.3 and 8.4.4.
8.5.4 Change report resulting from requirement 8.4.5.
9.5.1 Verification plan resulting from requirements 9.4.1.1 and 9.4.1.2.
9.5.2 Verification specification resulting from requirements 9.4.2.1 to 9.4.2.4.
9.5.3 Verification report resulting from requirements 9.4.3.1 to 9.4.3.4.
10.5.1 Documentation management plan resulting from requirement 10.4.1 and 10.4.2.
10.5.2 Documentation guideline requirements resulting from requirements 10.4.3 to 10.4.6.
11.5.1 Software tool criteria evaluation report resulting from requirements 11.4.1 to 11.4.5.
11.5.2 Software tool qualification report resulting from requirements 11.4.6 to 11.4.9.

Table A.1 (continued)

| Clause | Objectives                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Prerequisites                                                                                              | Work products                                                                                                                                                                                                                                                                                                   |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12     | The objective of the qualification of software components is to provide evidence for their suitability for re-use in items developed in compliance with the ISO 26262 series of standards.                                                                                                                                                                                                                                                                       | Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1 | 12.5.1 Software component documentation resulting from requirement 12.4.2.1. 12.5.2 Software component qualification report resulting from requirement 12.4.2.2 to 12.4.2.5. 12.5.3 Software component qualification verification report resulting from requirement 12.4.3.                                     |
| 13     | The objective of this Clause is to ensure that the functional behaviour is adequate to meet the allocated safety requirements and therefore the risk of a violation of a safety goal or of a safety requirement due to a systematic fault of the hardware element is sufficiently low. Suitability for use based on random fault management is established by the integrator of the evaluated hardware element, at the next highest level of design integration. | Organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1 | 13.5.1 Hardware element evaluation plan resulting from requirement 13.4.3.2. 13.5.2 Hardware element test plan if applicable, resulting from requirement 13.4.3.5.1. 13.5.3 Hardware element evaluation report for hardware elements resulting from requirement 13.4.1.1, 13.4.3.6 and 13.4.4.3, if applicable. |

In this Clause, the use of the term “hardware element” refers either to COTS hardware components or parts, or to custom hardware components or parts, that are not originally developed or designed according to the ISO 26262 series of standard and are considered to be safety-related within the context of the ISO 26262 compliant item or element in which they are to be integrated.

More precisely the evaluation of hardware elements is an alternative means of compliance with ISO 26262-5. The hardware elements eligible for evaluation can either be specific to an application or standard elements. Such elements are often developed for use across many industries either for automotive application or non-automotive application.

Table A.1 (continued)

| Clause | Objectives                                                                                                                                                                                                                                                                              | Prerequisites                                                                                                                                                                                                                           |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 14     | The objective of this Clause is to provide guidance for a proven in use argument. A proven in use argument is an alternate means of compliance with the ISO 26262 series of standards that may be used in the case of reuse of existing items or elements when field data is available. | Regarding the intended use of a candidate: — candidate specification; — applicable safety goal(s) or safety requirement(s) with corresponding ASIL(s); — foreseeable operational situation and intended operating modes and interfaces. |
| 14.5.1 | Description of candidate for proven in use argument resulting from requirement 14.4.3.                                                                                                                                                                                                  |                                                                                                                                                                                                                                         |
| 14.5.2 | Proven in use analysis reports resulting from requirements 14.4.4 to 14.4.5.                                                                                                                                                                                                            |                                                                                                                                                                                                                                         |
|        |                                                                                                                                                                                                                                                                                         | Regarding the previous use of a candidate: — field data from service period.                                                                                                                                                            |
| 15     | This Clause applies to T&B, where the objective is to achieve confidence that an application that is out of scope of ISO 26262 is not able to violate the safety goals of the base vehicle or item that has been developed in accordance with the ISO 26262 series of standards.        | Item definition in accordance with ISO 26262-3:2018, 5.5.1                                                                                                                                                                              |
| 15.5.1 | Base Vehicle Manufacturer or Supplier guideline resulting from requirements 15.4.2 and 15.4.3.                                                                                                                                                                                          |                                                                                                                                                                                                                                         |
| 16     | This Clause applies to T&B, where the objective is to achieve confidence that a system or component that is not developed according to ISO 26262 satisfies the required level of functional safety needed for the integration into an item developed according to ISO 26262.            | Item definition in accordance with ISO 26262-3:2018, 5.5.1                                                                                                                                                                              |
| 16.5.1 | Safety rationale resulting from requirements 16.4.2 to 16.4.4.                                                                                                                                                                                                                          |                                                                                                                                                                                                                                         |

# B (informative) Development Interface Agreement (DIA) example

# B.1 Purpose

This annex provides an illustrative example of a DIA, in accordance with the requirements of Clause 5
[especially 5.4.3.1 c) to k)], with organization-specific adaptation under the requirements and
recommendations of ISO 26262-2:2018, 5.4.6 and ISO 26262-2:2018, 5.5.1, if any. Project specific
tailoring, in accordance with ISO 26262-2:2018, 6.4.5, can also be applied.

# B.2 General

Many factors will affect the type and amount of customer-supplier interactions; the example is simplified,
based on an application scenario described in B.3 and a set of premises listed in B.4. Tables B.1 to B.3
constitute an example of a DIA as follows:

- Table B.1 approximately corresponds to the requirements of 5.4.2, with some organization-specific
  additions, intended to avoid or eliminate risk from a supplier with inadequate capability.
- Table B.2 approximately corresponds to the requirements of 5.4.3, with some organization-specific
  additions, intended to avoid or eliminate risk from improper understanding or definition of the
  boundary of Component C and its interactions with its environment.
- Table B.3 approximately corresponds to the requirements of 5.4.4, as applied to hardware
  Component C.

NOTE In each table, the corresponding ISO 26262 clause is indicated in parentheses.

# B.3 Application scenario

The DIA example shown in Tables B.1 to B.3 is based on the following application scenario:

- The customer is responsible for engineering and manufacturing the vehicle.
- The customer is responsible for engineering the system comprised of many hardware and software
  components of which one hardware component, C, is to be sourced from some supplier.
- Component C will be allocated requirements with assigned ASIL D.
- Component C has not been developed previously, i.e., it is not a commercial off-the-shelf (COTS)
  product. It involves new technology for which there is an inadequate pool of proven suppliers.
- Multiple suppliers are interested in the supply of Component C, but adequate capability to support
  the project is not evident.
- A model-based development process is used.

# B.4 Premises

This example is developed on the following premises:

- a) Resources required for project management and engineering are available when needed.
- b) Assessment teams that qualify as “independent” are available to each participating organization, and are used where needed.
- c) The same process and architectural framework is in use in all the participating organizations, independently assessed to qualify for the highest integrity level.
- — Reusable assets conform to the process and architectural framework, and are independently assessed to qualify for the required integrity level.
- — Other resources, e.g., tools, conform to the process and architectural framework, and are independently assessed to qualify for the required integrity level.
- — The participating organizations choose specific processes and tools that are compatible, and commit to the same architecture.
- — Explicit meta-models or specifications define unambiguously the semantics of the tools, modelling languages, programming languages, and the produced models.
- — Models of externally-visible behaviour, performance (including worst-case), and failure modes and effects are available for hardware components, including I/O devices. The models are in a form that can be correctly integrated to create (sub-)system models.
- d) There is high quality execution of other customer-supplier interactions, not unique to high integrity engineering, not included in this example, e.g., interactions for business processes, project management, and quality management.

In case the premises above do not hold, additional customer-supplier interactions and effort will be required — not identified in this example.

Table B.1 — Customer-supplier data exchanges to qualify and select supplier

| ID  | Activity                                                              | Data from customer to supplier                                                                                                                                                                                | Data from supplier to customer |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| A.1 | Pre-qualify suppliers; Project independent criteria; Feeds into 5.4.2 | Capability assessment questionnairea: — safety culture (ISO 26262-2:2018, 5.4.2); — evidence of competence (ISO 26262-2:2018, 5.4.4); — evidence of quality management (ISO 26262-2:2018, 5.4.5); — ISO 26262 | —                              |
| A.2 | Consent, e.g.:                                                        | — independent assessment (5.4.5); — DIA template                                                                                                                                                              | —                              |
| A.3 | —                                                                     | —                                                                                                                                                                                                             | —                              |
| A.4 | Qualify suppliers                                                     | Customer-organization-specific process adaptation of ISO 26262-2:2018, 5.4.6 incl. methods, languages, tools & usage constraints/guidelines.                                                                  | —                              |
| A.5 | 5.4.2                                                                 | Iterative evaluation & enquiries about gaps and alternativesa                                                                                                                                                 | —                              |
| A.6 | Send proposal                                                         | RFP/RFQ, including project-specific tailored process [5.4.3.1 b)], product concept i.e. item definition (ISO 26262-3:2018, 5.5.1) and safety goals (extracted from ISO 26262-3:2018, 6.5.1).                  | —                              |
| A.7 | —                                                                     | —                                                                                                                                                                                                             | —                              |
| A.8 | Select supplier                                                       | Proposed DIA (project-specific) 5.4.3                                                                                                                                                                         | —                              |

a Activity or data which is organization-specific and is not required in ISO 26262.

Acceptance of conditionsa

Capability assessmenta (ISO 26262-2:2018, Clause 5)

Disclosurea

Corrective action proposeda

—

First party assessment of compliance.

Disclosurea

Track record (5.4.2.1).

Corrective action proposeda

Alternative approach or proposal to meet objectivesa

Iterative revisions to plans and alternativesa

—

Offer;

Statement of compliance;

Updates to previously submitted informationa

—

Table B.1 (continued)

| ID   | Activity                                                       | Data from customer to supplier | Data from supplier to customer                                                                                                                                                                                                                                                                                     |
| ---- | -------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A.9  |                                                                | —                              | Selected project resources and their capability assessment, e.g. safety team members' skills, competencies and qualification (ISO 26262-2:2018, 5.5.2); Organization-specific rules and processes (ISO 26262-2:2018, 5.5.1), incl. tools, libraries; Preliminary plans, e.g. safety plan (ISO 26262-2:2018, 6.5.3) |
| A.10 | Iterative evaluation and enquiries, e.g. regarding skill gapsa | Acceptance of DIA.             | Acceptance of DIA                                                                                                                                                                                                                                                                                                  |
| A.11 | (5.5.2)                                                        | Selection report (5.5.1)       | Contract for concept (ISO 26262-3; ISO 26262-4) and planning phase (ISO 26262-2) incl. statement of development work.                                                                                                                                                                                              |
| A.12 |                                                                |                                | Acceptance.                                                                                                                                                                                                                                                                                                        |

a Activity or data which is organization-specific and is not required in ISO 26262.

Table B.2 — Customer-supplier data exchanges in project initiation and system concept

| ID  | Activity                                                                                                                                                                                   | Data from customer to supplier                                                                                                                          |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| B.1 | Initiate project (5.4.3)                                                                                                                                                                   | System level plans                                                                                                                                      |
|     | Create functional safety concept (ISO 26262-3:2018, Clauses 5 to 7)                                                                                                                        | Item definition (ISO 26262-3:2018, 5.5.1) and its lifecycle (Figure 1, ISO 26262-2:2018, 5.2.2; ISO 26262-2:2018, Figure 2 and ISO 26262-2:2018, 6.4.5) |
|     |                                                                                                                                                                                            | Functional safety concept (ISO 26262-3:2018, Clause 7)                                                                                                  |
| B.2 | —                                                                                                                                                                                          | —                                                                                                                                                       |
| B.3 | —                                                                                                                                                                                          | Acceptance                                                                                                                                              |
| B.4 | Consideration of experience gained from proven in use components, tools, libraries used in similar projects, as well as proven in use data and analyses of possible candidates (Clause 14) | Initial safety plan (ISO 26262-2:2018, Clause 5), incl. system safety case structure                                                                    |

Data from supplier to customer

—Safety plan (5.5.3)HARA (5.4.3.2), Hardware component behaviour models, incl. fault metrics [5.4.3.1 f), ISO 26262-5:2018, B, and ISO 26262-5:2018, Clause 9].Independent assessment of plans, incl. assurance that processes and resources are configured and allocated to match the required work products, incl. skill-sets. [5.4.3.1 c) e), g), j), 5.4.5]——

Table B.2 (continued)

| ID  | Activity                                  | Data from customer to supplier                                                                                                                                                                                                               | Data from supplier to customer                                                                                                                                                                                                |
| --- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| B.5 | —                                         | —                                                                                                                                                                                                                                            | (Clause 14), with independent assessment of fitness for the project (5.4.5)                                                                                                                                                   |
| B.6 | —                                         | Acceptance Technical safety concept (ISO 26262-4:2018, 6.5.2), relevant parts of system design specs, hardware specs, design & implementation (D&I) constraints, hardware-software Interface (HSI) specifications (ISO 26262-4:2018, 6.5.4). | Iterative evaluation, clarification-queries, and feedback about conflicts, completeness, consistency, etc.; technological limitations, if any; change requests, if any (5.4.4). Updated behaviour models, incl. fault models. |
| B.7 | System development lifecycle [5.4.3.1 c)] | —                                                                                                                                                                                                                                            | Feedback about boundary between Component C & its environment.                                                                                                                                                                |
| B.8 | —                                         | —                                                                                                                                                                                                                                            | Acceptance                                                                                                                                                                                                                    |

Table B.3 — Customer-supplier data exchanges in hardware development lifecycle

| ID  | Activity                                                          | Data from customer to supplier                | Data from supplier to customer                                                                                                                                                                                                                                |
| --- | ----------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C.1 | Authorisation for hardware development                            | Plan (5.4.3)                                  | —                                                                                                                                                                                                                                                             |
| C.2 | —                                                                 | —                                             | Plans: Safety plan (5.5.3 and ISO 26262-2:2018, 6.5.3), planning of DIA (5.4.3) etc. Independent reviews of conformance to planning (5.4.5).                                                                                                                  |
| C.3 | Acceptance. Authorisation to commence requirements specification. | —                                             | —                                                                                                                                                                                                                                                             |
| C.4 | Requirements (5.4.5 and ISO 26262-5)                              | —                                             | Hardware specifications - derived; refined; D&I constraints (ISO 26262-5:2018, 6.5.1). Extension to Verification Plan; HSI change requests, if any (ISO 26262-5:2018, 6.5.2). Independent safety audit (5.4.3.1); Independent confirmation (5.4.5 and 5.5.4). |
| C.5 | —                                                                 | Acceptance. Authorisation to commence design. | —                                                                                                                                                                                                                                                             |

Table B.3 (continued)

| ID   | Activity                                            | Data from customer to supplier                   |
| ---- | --------------------------------------------------- | ------------------------------------------------ |
| C.6  | Design (5.4.5, and ISO 26262-5)                     | —                                                |
| C.7  | Iterative evaluation and feedback                   | concerning conflicts discovered at system level. |
| C.8  | Acceptance of component design.                     | Authorisation to implement.                      |
| C.9  | —                                                   | Acceptance                                       |
| C.10 | —                                                   | —                                                |
| C.11 | Integrated evaluation (ISO 26262-4:2018, Clause 7). | Change requests, if any.                         |
| C.12 | —                                                   | —                                                |
| C.13 | —                                                   | Acceptance                                       |
| C.14 | —                                                   | —                                                |
| C.15 | Integrated evaluation (ISO 26262-4:2018, Clause 7)  | Change requests, if any.                         |

a Activity or data which is organization-specific and is not required in ISO 26262.

Data from supplier to customer

- Design specs (ISO 26262-5:2018, 7.5.1); implementation constraints, incl. architectural (ISO 26262-5:2018, Clause 8).
- Extension or modification to HARA (ISO 26262-3:2018, Clause 6), if any.
- Extension to item integration and testing plan (ISO 26262-5:2018, 10.5).
- HSI change requests, if any (ISO 26262-5:2018, 6.5.2).
- Independent safety audit (5.4.3.1, 5.4.5)
- Iterative clarifications, revisions, and other responses addressing customer feedback and enquiries.
- Independent assessment (5.4.5 and 5.5.4).
- Implementation.
- Requirements from the environment.
- Independent assessment (5.4.5 and 5.5.4).
- —
- Prototype part
- Integrated verification (ISO 26262-5:2018, 10.5)
- Independent assessment (5.4.5).
- —
- Reviews & audits of processed changes
- Independent assessment (5.4.5, 5.5.4).
- —
- Sample for series production
- Independent assessment (5.4.5, 5.5.4).
- —

Table B.3 (continued)

| ID   | Activity | Data from customer to supplier                | Data from supplier to customer                                  |
| ---- | -------- | --------------------------------------------- | --------------------------------------------------------------- |
| C.16 | —        | —                                             | Independent assessment (5.4.4, 5.4.5 and 5.5.4).                |
| C.17 | —        | Authorisation for commencing production phase | —                                                               |
| C.18 | —        | —                                             | Post-SOP reports (5.4.6 and 5.5.5 and ISO 26262-2:2018, 7.5.1). |

a Activity or data which is organization-specific and is not required in ISO 26262.

# Bibliography

| [1]  | ISO 26262-11:2018, Road vehicles — Functional safety — Part 11: Guideline on application of ISO 26262 to semiconductors |
| ---- | ----------------------------------------------------------------------------------------------------------------------- |
| [2]  | ISO 26262-12:2018, Road vehicles — Functional safety — Part 12: Adaptation of ISO 26262 for motorcycles                 |
| [3]  | ISO 9001, Quality management systems — Requirements                                                                     |
| [4]  | ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes                                      |
| [5]  | ISO 16750 (all parts), Road vehicles — Environmental conditions and testing for electrical and electronic equipment     |
| [6]  | IATF 16949, Quality management system requirements for automotive production and relevant service parts organizations   |
| [7]  | ISO 25119 (all parts), Tractors and machinery for agriculture and forestry — Safety‑related parts of control systems    |
| [8]  | ISO/IEC/IEEE 29148, Systems and software engineering — Life cycle processes — Requirements engineering                  |
| [9]  | ISO 13849 (all parts), Safety of machinery — Safety‑related parts of control systems                                    |
| [10] | IEC 61508 (all parts), Functional safety of electrical/electronic/programmable electronic safety‑related systems        |
| [11] | RTCA DO-178C, Software Considerations in Airborne Systems and Equipment Certification                                   |
| [12] | CMMI for Development, CMMI-DEV, Carnegie Mellon University Software Engineering Institute.                              |
| [13] | German V-Model - Available at: http://www.v-modell-xt.de/ [viewed 2018-09-27]                                           |
| [14] | AEC Q100. Failure Mechanism Based Stress Test Qualification For Integrated Circuits                                     |
| [15] | AEC Q101. Failure Mechanism Based Stress Test Qualification For Discrete Semiconductors                                 |
| [16] | AEC Q200. Stress Test Qualification For Passive Components                                                              |
| [17] | Automotive SPICE®4) - Available at: http://www.automotivespice.com [viewed 2018-09-27]                                  |
| [18] | ISO 10007, Quality management — Guidelines for configuration management                                                 |
| [19] | ISO/IEC/IEEE 12207, Systems and software engineering — Software life cycle processes                                    |
| [20] | ISO/IEC 33000 (series), Information Technology — Process Assessment                                                     |

4. Automotive SPICE® is an example of a suitable product available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by ISO of these products.
