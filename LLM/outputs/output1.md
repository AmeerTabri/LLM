# 1 Scope



# 1.1 ???



This European Standard specifies the process and technical requirements for the development of software for programmable electronic systems for use in railway control and protection applications. It is aimed at use in any area where there are safety implications. These systems can be implemented using dedicated microprocessors, programmable logic controllers, multiprocessor distributed systems, larger scale central processor systems or other architectures.



# 1.2 ???



This European Standard is applicable exclusively to software and the interaction between software and the system of which it is part.



# 1.3 ???



This European Standard is not relevant for software that has been identified as having no impact on safety, i.e. software of which failures cannot affect any identified safety functions.



# 1.4 ???



This European Standard applies to all safety related software used in railway control and protection systems, including



- application programming,

- operating systems,

- support tools,

- firmware.



Application programming comprises high level programming, low level programming and special purpose programming (for example: Programmable logic controller ladder logic).



# 1.5 ???



This European Standard also addresses the use of pre-existing software and tools. Such software may be used, if the specific requirements in 7.3.4.7 and 6.5.4.16 on pre-existing software and for tools in 6.7 are fulfilled.



# 1.6 ???



Software developed according to any version of this European Standard will be considered as compliant and not subject to the requirements on pre-existing software.



# 1.7 ???



This European Standard considers that modern application design often makes use of generic software that is suitable as a basis for various applications. Such generic software is then configured by data, algorithms, or both, for producing the executable software for the application. The general Clauses 1 to 6 and 9 of this European Standard apply to generic software as well as for application data or algorithms. The specific Clause 7 applies only for generic software while Clause 8 provides the specific requirements for application data or algorithms.



# 1.8 ???



This European Standard is not intended to address commercial issues. These should be addressed as an essential part of any contractual agreement. All the clauses of this European Standard will need careful consideration in any commercial situation.



# 1.9 ???



This European Standard is not intended to be retrospective. It therefore applies primarily to new developments and only applies in its entirety to existing systems if these are subjected to major modifications. For minor changes, only 9.2 applies. The assessor has to analyse the evidences provided in the software documentation to confirm whether the determination of the nature and scope of software changes is adequate. However, application of this European Standard during upgrades and maintenance of existing software is highly recommended.



# 2 Normative references



The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.



| EN 50126-1:1999     | Railway applications – The specification and demonstration of Reliability, Availability, Maintainability and Safety (RAMS) – Part 1: Basic requirements and generic process |

| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| EN 50129:2003       | Railway applications – Communication, signalling and processing systems – Safety related electronic systems for signalling                                                  |

| EN ISO 9000         | Quality management systems – Fundamentals and vocabulary (ISO 9000:2005)                                                                                                    |

| EN ISO 9001         | Quality management systems – Requirements (ISO 9001:2008)                                                                                                                   |

| ISO/IEC 90003:2004  | Software engineering – Guidelines for the application of ISO 9001:2000 to computer software                                                                                 |

| ISO/IEC 9126 series | Software engineering – Product quality                                                                                                                                      |



# 3 Terms, definitions and abbreviations



# 3.1 Terms and definitions



For the purposes of this document, the following terms and definitions apply.



# 3.1.1 assessment



process of analysis to determine whether software, which may include process, documentation, system, subsystem hardware and/or software components, meets the specified requirements and to form a judgement as to whether the software is fit for its intended purpose. Safety assessment is focused on but not limited to the safety properties of a system



# 3.1.2 assessor



entity that carries out an assessment



# 3.1.3 commercial off-the-shelf (COTS) software



software defined by market-driven need, commercially available and whose fitness for purpose has been demonstrated by a broad spectrum of commercial users



# 3.1.4 component



a constituent part of software which has well-defined interfaces and behaviour with respect to the software architecture and design and fulfils the following criteria:



- it is designed according to “Components” (see Table A.20);

- it covers a specific subset of software requirements;



# 3.1.5 configuration manager



entity that is responsible for implementing and carrying out the processes for the configuration management of documents, software and related tools including change management



# 3.1.6 customer



entity which purchases a railway control and protection system including the software



# 3.1.7 designer



entity that analyses and transforms specified requirements into acceptable design solutions which have the required safety integrity level



# 3.1.8 entity



person, group or organisation who fulfils a role as defined in this European Standard



# 3.1.9 error, fault



defect, mistake or inaccuracy which could result in failure or in a deviation from the intended performance or behaviour



# 3.1.10 failure



unacceptable difference between required and observed performance



# 3.1.11 fault tolerance



built-in capability of a system to provide continued correct provision of service as specified, in the presence of a limited number of hardware or software faults



# 3.1.12 firmware



software stored in read-only memory or in semi-permanent storage such as flash memory, in a way that is functionally independent of applicative software



# 3.1.13 generic software



software which can be used for a variety of installations purely by the provision of application-specific data and/or algorithms



# 3.1.14 implementer



entity that transforms specified designs into their physical realisation



# 3.1.15 integration



process of assembling software and/or hardware items, according to the architectural and design specification, and testing the integrated unit



# 3.1.16 integrator



entity that carries out software integration



# 3.1.17 pre-existing software



software developed prior to the application currently in question, including COTS (commercial off-the shelf) and open source software



# 3.1.18 open source software



source code available to the general public with relaxed or non-existent copyright restrictions



# 3.1.19 programmable logic controller



solid-state control system which has a user programmable memory for storage of instructions to implement specific functions



# 3.1.20 project management



administrative and/or technical conduct of a project, including safety aspects



# 3.1.21 project manager



entity that carries out project management



# 3.1.22 reliability



ability of an item to perform a required function under given conditions for a given period of time



# 3.1.23 robustness



ability of an item to detect and handle abnormal situations



# 3.1.24 requirements manager



entity that carries out requirements management



# 3.1.25 requirements management



the process of eliciting, documenting, analysing, prioritising and agreeing on requirements and then controlling change and communicating to relevant stakeholders. It is a continuous process throughout a project



# 3.1.26 risk



combination of the rate of occurrence of accidents and incidents resulting in harm (caused by a hazard) and the degree of severity of that harm



# 3.1.27 safety



freedom from unacceptable levels of risk of harm to people



# 3.1.28 safety authority



body responsible for certifying that safety related software or services comply with relevant statutory safety requirements



# 3.1.29 safety function



a function that implements a part or whole of a safety requirement



# 3.1.30 safety-related software



software which performs safety functions



# 3.1.31 software



intellectual creation comprising the programs, procedures, rules, data and any associated documentation pertaining to the operation of a system



# 3.1.32 software baseline



complete and consistent set of source code, executable files, configuration files, installation scripts and documentation that are needed for a software release. Information about compilers, operating systems, pre-existing software and dependent tools is stored as part of the baseline. This will enable the organisation to



# 3.1.33 software deployment



transferring, installing and activating a deliverable software baseline that has already been released and assessed



# 3.1.34 software life-cycle



those activities occurring during a period of time that starts when software is conceived and ends when the software is no longer available for use. The software lifecycle typically includes a requirements phase, design phase, test phase, integration phase, deployment phase and a maintenance phase



# 3.1.35 software maintainability



capability of the software to be modified; to correct faults, improve performance or other attributes, or adapt it to a different environment



# 3.1.36 software maintenance



action, or set of actions, carried out on software after deployment with the aim of enhancing or correcting its functionality



# 3.1.37 software safety integrity level



classification number which determines the techniques and measures that have to be applied to software



NOTE Safety-related software has been classified into five safety integrity levels, where 0 is the lowest and 4 the highest.



# 3.1.38 supplier



entity that designs and builds a railway control and protection system including the software or parts thereof



# 3.1.39 system safety integrity level



classification number which indicates the required degree of confidence that an integrated system comprising hardware and software will meet its specified safety requirements



# 3.1.40 tester



an entity that carries out testing



# 3.1.41 testing



process of executing software under controlled conditions as to ascertain its behaviour and performance compared to the corresponding requirements specification



# 3.1.42 tool class T1



generates no outputs which can directly or indirectly contribute to the executable code (including data) of the software



NOTE T1 examples include: a text editor or a requirement or design support tool with no automatic code generation capabilities; configuration control tools.



# 3.1.43 tool class T2



supports the test or verification of the design or executable code, where errors in the tool can fail to reveal defects but cannot directly create errors in the executable software



NOTE T2 examples include: a test harness generator; a test coverage measurement tool; a static analysis tool.



# 3.1.44 tool class T3



generates outputs which can directly or indirectly contribute to the executable code (including data) of the safety related system



NOTE T3 examples include: a source code compiler, a data/algorithms compiler, a tool to change set-points during system operation; an optimising compiler where the relationship between the source code program and the generated object code is not obvious; a compiler that incorporates an executable run-time package into the executable code.



# 3.1.45 traceability



degree to which a relationship can be established between two or more products of a development process, especially those having a predecessor/successor or master/subordinate relationship to one another



# 3.1.46 validation



process of analysis followed by a judgment based on evidence to determine whether an item (e.g. process, documentation, software or application) fits the user needs, in particular with respect to safety and quality and with emphasis on the suitability of its operation in accordance to its purpose in its intended environment



# 3.1.47 validator



entity that is responsible for the validation



# 3.1.48 verification



process of examination followed by a judgment based on evidence that output items (process, documentation, software or application) of a specific development phase fulfils the requirements of that phase with respect to completeness, correctness and consistency



NOTE Verification is mostly based on document reviews (design, implementation, test documents etc.).



# 3.1.49 verifier



entity that is responsible for one or more verification activities



# 3.2 Abbreviations



For the purposes of this document, the following abbreviations apply.



| ASR    | Assessor                                                      |

| ------ | ------------------------------------------------------------- |

| COTS   | Commercial off-the-shelf                                      |

| DES    | Designer                                                      |

| HR     | Highly Recommended                                            |

| IMP    | Implementer                                                   |

| INT    | Integrator                                                    |

| JSD    | Jackson System Development Method                             |

| M      | Mandatory                                                     |

| MASCOT | Modular Approach to Software Construction, Operation and Test |

| NR     | Not Recommended                                               |

| PM     | Project Manager                                               |

| R      | Recommended                                                   |

| RAMS   | Reliability, Availability, Maintainability and Safety         |



| RQM   | Requirements Manager                             |

| ----- | ------------------------------------------------ |

| SDL   | Specification and Description Language           |

| SFC   | Sequential Function Charts                       |

| SIL   | Safety Integrity Level                           |

| SOM   | Service Oriented Modeling                        |

| SSADM | Structured Systems Analysis & Design Methodology |

| TST   | Tester                                           |

| V&V   | Verification and Validation                      |

| VAL   | Validator                                        |

| VER   | Verifier                                         |



# 4 Objectives, conformance and software safety integrity levels



# 4.1 ???



The allocation of safety-related system functions to software, as well as software interfaces, shall be identified in the system documentation. The system in which the software is embedded shall be fully defined with respect to the following:



- functions and interfaces;

- application conditions;

- configuration or architecture of the system;

- hazards to be controlled;

- safety integrity requirements;

- apportionment of requirements and allocation of SIL to software and hardware;

- timing constraints



NOTE The allocation of safety integrity requirements may lead to different SIL for well-separated software and hardware parts of a subsystem. This allocation depends on the contribution of the software and hardware parts of the subsystem to the safety-related functions and on the mechanisms for the failure mitigation including the separation of function with different SIL.



# 4.2 ???



The software safety integrity shall be specified as one of five levels, from SIL 0 (the lowest) to SIL 4 (the highest).



# 4.3 ???



The required software safety integrity level shall be decided and assessed at system level, on the basis of the system safety integrity level and the level of risk associated with the use of the software in the system.



# 4.4 ???



At least the SIL 0 requirements of this European Standard shall be fulfilled for the software part of functions that have a safety impact below SIL 1. This is because uncertainty is present in the evaluation of the risk, and even in the identification of hazards. In the face of uncertainty it is prudent to aim for a low level of safety integrity, represented by SIL 0, rather than none.



# 4.5 ???



To conform to this European Standard it shall be shown that each of the requirements has been satisfied to the software safety integrity level defined and therefore the objective of the sub-clause in question has been met.



# 4.6 ???



Where a requirement is qualified by the words _to the extent required by the software safety integrity level_, this indicates that a range of techniques and measures shall be used to satisfy that requirement.



# 4.7 ???



Where 4.6 is applied, tables from normative A shall be used to assist in the selection of techniques and measures appropriate to the software safety integrity level. The selection shall be



# 4.8 ???



If a technique or measure which is ranked as highly recommended (HR) in the tables is not used, then the rationale for using alternative techniques shall be detailed and recorded either in the Software Quality Assurance Plan or in another document referenced by the Software Quality Assurance Plan. This is not necessary if an approved combination of techniques given in the corresponding table is used. The selected techniques shall be demonstrated to have been applied correctly.



# 4.9 ???



If a technique or measure is proposed to be used that is not contained in the tables then its effectiveness and suitability in meeting the particular requirement and overall objective of the sub-clause shall be justified and recorded in either the Software Quality Assurance Plan or in another document referenced by the Software Quality Assurance Plan.



# 4.10 ???



Compliance with the requirements of a particular sub-clause and their respective techniques and measures detailed in the tables shall be verified by the inspection of documents required by this European Standard. Where appropriate, other objective evidence, auditing and the witnessing of tests shall also be taken into account.



# 5 Software management and organisation



# 5.1 Organisation, roles and responsibilities



# 5.1.1 Objective



# 5.1.1.1 ???



To ensure that all personnel who have responsibilities for the software are organised, empowered and capable of fulfilling their responsibilities.



# 5.1.2 Requirements



# 5.1.2.1 ???



As a minimum, the supplier shall implement the parts of EN ISO 9001 dealing with the organisation and management of the personnel and responsibilities.



# 5.1.2.2 ???



Responsibilities shall be compliant with the requirements defined in B.



# 5.1.2.3 ???



The personnel assigned to the roles involved in the development or maintenance of the software shall be named and recorded.



# 5.1.2.4 ???



An Assessor shall be appointed by the supplier, the customer or the Safety Authority.



# 5.1.2.5 ???



The Assessor shall be independent from the supplier or, at the discretion of the Safety Authority, be part of the supplier’s organisation or of the customer’s organisation.



# 5.1.2.6 ???



The Assessor shall be independent from the project.



# 5.1.2.7 ???



The Assessor shall be given authority to perform the assessment of the software.



# 5.1.2.8 ???



The Validator shall give agreement/disagreement for the software release.



# 5.1.2.9 ???



|     | SIL3 & SIL4  |     | RQM, DES, IMP | INT, TST           | VER      | VAL |

| --- | ------------ | --- | ------------- | ------------------ | -------- | --- |

|     | SIL 1 & SIL2 |     | RQM, DES, IMP | INT, TST           | VER, VAL |     |

|     | SIL0         |     | RQM, DES, IMP | INT, TST, VER, VAL |          |     |



# Key



- can be the same person

- can be the same organization

- shall report to the Project Manager

- can report to the Project Manager

- shall not report to the Project Manager



| PM  | Project Manager      |

| --- | -------------------- |

| ASR | Assessor             |

| RQM | Requirements Manager |

| INT | Integrator           |

| TST | Tester               |

| DES | Designer             |

| IMP | Implementer          |

| VER | Verifier             |

| VAL | Validator            |



NOTE: For the role of the Configuration Manager, see Table B.10, there are no independence requirements.



Figure 2 – Illustration of the preferred organisational structure



NOTE: Figure 2 is only illustrative for the preferred organisational structure.



# 5.1.2.10 ???



The preferred organisational structure for SIL 3 and SIL 4 is:



1. Requirements Manager, Designer and Implementer for a software component can be the same person.

2. Requirements Manager, Designer and Implementer for a software component shall report to the Project Manager.

3. Integrator and Tester for a software component can be the same person.

4. Integrator and Tester for a software component can report to the Project Manager or to the Validator.

5. Verifier can report to the Project Manager or to the Validator.

6. Validator shall not report to the Project Manager i.e. the Project Manager shall have no influence on the validator’s decisions but the validator informs the Project Manager about his decisions.

7. A person who is Requirements Manager, Designer or Implementer for a software component shall neither be Tester nor Integrator for the same software component.

8. A person who is Integrator or Tester for a software component shall neither be Requirements Manager, Designer nor Implementer for the same software component.

9. A person who is Verifier shall neither be Requirements Manager, Designer, Implementer, Integrator, Tester nor Validator.

10. A person who is Validator shall neither be Requirements Manager, Designer, Implementer, Integrator, Tester nor Verifier.

11. A person who is Project Manager can additionally perform the roles of Requirements Manager, Designer, Implementer, Integrator, Tester or Verifier providing that the requirements for the independence between these additional roles are respected.

12. Project Manager, Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier and Validator can belong to the same organization.

13. The assessor shall be independent and organisationally independent from the roles of Project Manager, Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier and Validator.



However, the following options may apply:



A person who is Validator may also perform the role of Verifier, but still maintaining independence from the Project Manager. In this case the Verifier’s output documents shall be reviewed by another competent person with the same level of independence as the Validator. This organisational option shall be subject to Assessor’s approval.

A person who is Verifier may also perform the role of Integrator and Tester, in which case the role of Validator shall check the adequacy of the documented evidence from integration and testing with the specified verification objectives, hence maintaining two levels of checking within the project organisation.



# 5.1.2.11 ???



The preferred organisational structure for SIL 1 and SIL 2 is:



1. Requirements Manager, Designer and Implementer for a software component can be the same person and shall report to the Project Manager.

2. Integrator and Tester for a software component can be the same person.

3. Integrator and Tester for a software component can report to the Project Manager or to the Validator.

4. Verifier and Validator can be the same person.

5. Verifier and Validator can report to the Project Manager.

6. A person who is Requirements Manager, Designer or Implementer for a software component shall be neither Tester nor Integrator for the same software component.

7. A person who is Integrator or Tester for a software component shall neither be Requirements Manager, Designer nor Implementer for the same software component.

8. A person who is Verifier or Validator shall neither be Requirements Manager, Designer, Implementer, Integrator nor Tester.

9. A person who is a Project Manager can additionally perform the roles of Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier or Validator provided that the requirements for the independence between these additional roles are respected.

10. Project Manager, Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier and Validator can belong to the same organization.

11. The assessor shall be independent and organisationally independent from the roles of Project Manager, Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier and Validator.



# 5.1.2.12 ???



The preferred organisational structure for SIL 0 is:



- a) Requirements Manager, Designer and Implementer for a software component can be the same person and shall be managed by the Project Manager.

- b) Integrator, Tester, Verifier and Validator for a software component can be the same person.

- c) Integrator, Tester, Verifier and Validator can be managed by the Project Manager.

- d) A person who is Requirements Manager, Designer or Implementer for a software component shall be neither Tester nor Integrator for the same software component.

- e) A person who is Verifier or Validator shall neither be Requirements Manager, Designer, nor Implementer.

- f) A person who is Project Manager can additionally perform the roles of Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier or Validator providing that the requirements for the independence between these additional roles are respected.

- g) Project Manager, Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier and Validator can belong to the same organization.

- h) The assessor shall be independent and organisationally independent from the roles of Project Manager, Requirements Manager, Designer, Implementer, Integrator, Tester, Verifier and Validator.



However, the following alternatives can apply:



- i) Requirements Manager, Designer, Implementer, Integrator and Tester can be the same person.

- j) The Validator and Verifier can also be the same person;

- k) A person who is Verifier or Validator shall neither be Requirements Manager, Designer, nor Implementer.



# 5.1.2.13 ???



The roles Requirements Manager, Designer and Implementer for one component can perform the roles Tester and Integrator for a different component.



# 5.1.2.14 ???



The roles of the Verifier and the Validator shall be defined at the project level and shall remain unchanged throughout the development project.



# 5.2 Personnel competence



# 5.2.1 Objectives



# 5.2.1.1 ???



To ensure that all personnel who have responsibilities for the software are competent to discharge those responsibilities by demonstrating the ability to perform relevant tasks correctly, efficiently and consistently to a high quality and under varying conditions.



# 5.2.2 Requirements



# 5.2.2.1 ???



The key competencies required for each role in the software development are defined in B. If additional experience, capabilities or qualifications are required for a role in the software life cycle, these shall be defined in the Software Quality Assurance Plan.



# 5.2.2.2 ???



Documented evidence of personnel competence, including technical knowledge, qualifications, relevant experience and appropriate training, shall be maintained by the supplier’s organisation in order to demonstrate appropriate safety organisation.



# 5.2.2.3 ???



The organisation shall maintain procedures to manage the competence of personnel to suit appropriate roles in accordance to existing quality standards.



# 5.2.2.4 ???



Once it has been proved to the satisfaction of an assessor or by a certification that competence has been demonstrated for all personnel appointed in various roles, each individual will need to show continuous maintenance and development of competence. This could be demonstrated by keeping a logbook showing the activity is being regularly carried out correctly, and that additional training is being undertaken in accordance with EN ISO 9001 and ISO/IEC 90003:2004, 6.2.2 “Competence, awareness and training\_.



# 5.3 Lifecycle issues and documentation



# 5.3.1 Objectives



# 5.3.1.1 ???



To structure the development of the software into defined phases and activities.



# 5.3.1.2 ???



To record all information pertinent to the software throughout the lifecycle of the software.



# 5.3.2 Requirements



# 5.3.2.1 ???



A lifecycle model for the development of software shall be selected. It shall be detailed in the Software Quality Assurance Plan in accordance with 6.5.



Two examples of lifecycle models are shown in Figure 3 and Figure 4.



# 5.3.2.2 ???



The lifecycle model shall take into account the possibility of iterations in and between phases.



# 5.3.2.3 ???



Quality Assurance procedures shall run in parallel with lifecycle activities and use the same terminology.



# 5.3.2.4 ???



The Software Quality Assurance Plan, Software Verification Plan, Software Validation Plan and Software Configuration Management Plan shall be drawn up at the start of the project and maintained throughout the software development life cycle.



# 5.3.2.5 ???



All activities to be performed during a phase shall be defined and planned prior to the commencement of the phase.



# 5.3.2.6 ???



All documents shall be structured to allow continued expansion in parallel with the development process.



# 5.3.2.7 ???



For each document, traceability shall be provided in terms of a unique reference number and a defined and documented relationship with other documents.



# 5.3.2.8 ???



Each term, acronym or abbreviation shall have the same meaning in every document. If, for historical reasons, this is not possible, the different meanings shall be listed and the references given.



# 5.3.2.9 ???



Except for documents relating to pre-existing software (see 7.3.4.7), each document shall be written according to the following rules:



- it shall contain or implement all applicable conditions and requirements of the preceding document with which it has a hierarchical relationship;

- it shall not contradict the preceding document.



# 5.3.2.10 ???



Each item or concept shall be referred to by the same name or description in every document.



# 5.3.2.11 ???



The contents of all documents shall be recorded in a form appropriate for manipulation, processing and storage.



# 5.3.2.12 ???



When documents which are produced by independent roles are combined into a single document, the relation to the parts produced by any independent role shall be traced within the document.



# 5.3.2.13 ???



Documents may be combined or divided in accordance with 5.3.2.12. Some development steps may be combined, divided or, when justified, eliminated, at the discretion of the Project Manager and with the agreement of the Validator.



# 5.3.2.14 ???



Where any alternative lifecycle or documentation structure is adopted it shall be established that it meets all the objectives and requirements of this European Standard.



| DESIGN AND TEST DOCUMENTS                         | DESIGN AND TEST DOCUMENTS                                  | VERIFICATION ACTIVITIES                | PHASE                           |

| ------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------- | ------------------------------- |

| System Requirements Specification                 | System Safety Requirements Specification                   | System Architecture Description        | System Safety Plan and V&V Plan |

| Software Requirements Specification               | Overall Software Test Specification                        | Software Requirements Verification     | Software Requirements           |

| Software Architecture Specification               |                                                            | Software Architecture Verification     | Software Architecture           |

| Software Design Specification                     | Software, Software/Hardware Integration Test Specification | Software Design Verification           | Software Design                 |

| Software Component Design Specification           | Software Component Test Specification                      | Software Component Design Verification | Software Component              |

| Software Source Code and supporting documentation |                                                            | Component Implementation and Testing   |                                 |

| Software Component Test Report                    | Source Code Verification                                   | Software Integration Test Report       |                                 |

| Software/Hardware Integration Test Report         | Overall Software Test Report                               | Software Validation                    | Software Validation             |

| Software Deployment Documents                     |                                                            | Software Deployment                    |                                 |

| Software Maintenance Documents                    |                                                            | Software Maintenance                   |                                 |



Software assessment is an external activity and can be performed during the whole life-cycle.



Figure 3 – Illustrative Development Lifecycle 1



# System Development Phase (external)



- System Requirements Specification

- System Safety Requirements Specification

- System Architecture Description

- System Safety Plan



# Software Requirements Phase (7.2)



- Software Requirements Specification

- Overall Software Test Specification

- Software Requirements Verification Report



# Software Planning Phase



- Software Quality Assurance Plan



# Software Arch. & Design Phase (7.3)



- Software Configuration Management Plan

- Software Architecture Specification

- Software Verification Plan

- Software Design Specification

- Software Validation Plan

- Software Interface Specification

- Software Integration Test Specification

- Software/Hardware Integration Test Specification

- Software Architecture and Design Verification Report



# Software Maintenance Phase (9.2)



- Software Maintenance Records

- Software Change Records



# Software Assessment Phase



- Software Assessment Plan

- Software Assessment Report



# Software Validation Phase (7.7)



- Overall Software Test Report

- Software Validation Report



# Software Integration Phase (7.6)



- Software Integration Test Report

- Software/Hardware Integration Test Report

- Software Integration Verification Report



# Software Component Design Phase (7.4)



- Software Component Design Specification

- Software Component Test Specification

- Software Component Design Verification Report



# Software Component Testing Phase (7.5)



- Software Component Test Report

- Software Source Code Verification Report



# Software Component Implementation Phase (7.5)



- Software Source Code & Supporting Documentation



Figure 4 – Illustrative Development Lifecycle 2



# 6 Software assurance



# 6.1 Software testing



# 6.1.1 Objective



# 6.1.1.1 ???



The objective of software testing, as performed by the Tester and/or Integrator, is to ascertain the behaviour or performance of software against the corresponding test specification to the extent achievable by the selected test coverage.



# 6.1.2 Input documents



1. All necessary System, Hardware and Software Documentation as specified in the Software Verification Plan.



# 6.1.3 Output documents



1. Overall Software Test Specification

2. Overall Software Test Report

3. Software Integration Test Specification

4. Software Integration Test Report

5. Software/Hardware Integration Test Specification

6. Software/Hardware Integration Test Report

7. Software Component Test Specification

8. Software Component Test Report



# 6.1.4 Requirements



# 6.1.4.1 ???



Tests performed by other parties such as the Requirements Manager, Designer or Implementer, if fully documented and complying with the following requirements, may be accepted by the Verifier.



# 6.1.4.2 ???



Measurement equipment used for testing shall be calibrated appropriately. Any tools, hardware or software, used for testing shall be shown to be suitable for the purpose.



# 6.1.4.3 ???



Software testing shall be documented by a Test Specification and a Test Report, as defined in the following.



# 6.1.4.4 ???



Each Test Specification shall document the following:



- a) test objectives;

- b) test cases, test data and expected results;

- c) types of tests to be performed;

- d) test environment, tools, configuration and programs;

- e) test criteria on which the completion of the test will be judged;

- f) the criteria and degree of test coverage to be achieved;

- g) the roles and responsibilities of the personnel involved in the test process;

- h) the requirements which are covered by the test specification;

- i) the selection and utilisation of the software test equipment;



# 6.1.4.5 ???



A Test Report shall be produced as follows:



- a) the Test Report shall mention the Tester names, state the test results and whether the test objectives and test criteria of the Test Specification have been met. Failures shall be documented and summarized;

- b) test cases and their results shall be recorded, preferably in a machine-readable form for subsequent analysis;

- c) tests shall be repeatable and, if practicable, be performed by automatic means;

- d) test scripts for automatic test execution shall be verified;

- e) the identity and configuration of all items involved (hardware used, software used, equipment used, equipment calibration, as well as version information of the test specification) shall be documented;

- f) an evaluation of the test coverage and test completion shall be provided and any deviations noted.



# 6.2 Software verification



# 6.2.1 Objective



# 6.2.1.1 ???



The objective of software verification is to examine and arrive at a judgment based on evidence that output items (process, documentation, software or application) of a specific development phase fulfil the requirements and plans with respect to completeness, correctness and consistency. These activities are managed by the Verifier.



# 6.2.2 Input documents



1. All necessary System, Hardware and Software Documentation.



# 6.2.3 Output documents



1. Software Verification Plan

2. Software Verification Report(s)

3. Software Quality Assurance Verification Report



# 6.2.4 Requirements



# 6.2.4.1 ???



Verification shall be documented by at least a Software Verification Plan and one or more (process-related) Verification Reports.



# 6.2.4.2 ???



A Software Verification Plan shall be written, under the responsibility of the Verifier, on the basis of the necessary documentation.



Requirements from 6.2.4.3 to 6.2.4.9 refer to the Software Verification Plan.



# 6.2.4.3 ???



The Software Verification Plan shall describe the activities to be performed to ensure proper verification and that particular design or other verification needs are suitably provided for.



# 6.2.4.4 ???



During development (and depending upon the size of the system) the plan may be sub-divided into a number of child documents and be added to, as the detailed needs of verification become clearer.



# 6.2.4.5 ???



The Software Verification Plan shall document all the criteria, techniques and tools to be used in the verification process. The Software Verification Plan shall include techniques and measures chosen from Table A.5, Table A.6, Table A.7 and Table A.8. The selected combination shall be justified as a set satisfying 4.8, 4.9 and 4.10.



# 6.2.4.6 ???



The Software Verification Plan shall describe the activities to be performed to ensure correctness and consistency with respect to the input to that phase. These include reviewing, testing and integration.



# 6.2.4.7 ???



In each development phase it shall be shown that the functional, performance and safety requirements are met.



# 6.2.4.8 ???



The results of each verification shall be retained in a format defined or referenced in the Software Verification Plan.



# 6.2.4.9 ???



The Software Verification Plan shall address the following:



- a) the selection of verification strategies and techniques (to avoid undue complexity in the assessment of the verification and testing, preference shall be given to the selection of techniques which are in themselves readily analysable);

- b) selection of techniques from Table A.5, Table A.6, Table A.7 and Table A.8;






c) the selection and documentation of verification activities;



d) the evaluation of verification results gained;



e) the evaluation of the safety and robustness requirements;



f) the roles and responsibilities of the personnel involved in the verification process;



g) the degree of the functional based test coverage required to be achieved;



h) the structure and content of each verification step, especially for the Software Requirement Verification (7.2.4.22), Software Architecture and Design Verification (7.3.4.41, 7.3.4.42), Software Components Verification (7.4.4.13), Software Source Code Verification (7.5.4.10) and Integration Verification (7.6.4.13) in a way that facilitates review against the Software Verification Plan.



# 6.2.4.10 ???



A Software Quality Assurance Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 6.2.2.



# 6.2.4.11 ???



Once the Software Verification Plan has been established, verification shall address



a) that the Software Verification Plan meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 6.2.4.3 to 6.2.4.9,



b) the internal consistency of the Software Verification Plan.



The results shall be recorded in a Software Quality Assurance Verification Report.



# 6.2.4.12 ???



Any Software Verification Reports shall be written, under the responsibility of the Verifier, on the basis of the input documents. These reports can be partitioned for clarity and convenience, and shall follow the Software Verification Plan. The requirement in 6.2.4.13 refers to the Software Verification Reports.



# 6.2.4.13 ???



Each Software Verification Report shall document the following:



a) the identity and configuration of the items verified, as well as the Verifier names;



b) items which do not conform to the specifications;



c) components, data, structures and algorithms poorly adapted to the problem;



d) detected errors or deficiencies;



e) the fulfilment of, or deviation from, the Software Verification Plan (in the event of deviation the Verification Report shall explain whether the deviation is critical or not);



f) assumptions if any;



g) a summary of the verification results.



# 6.3 Software validation



# 6.3.1 Objective



# 6.3.1.1 ???



The objective of software validation is to demonstrate that the processes and their outputs are such that the software is of the defined software safety integrity level, fulfils the software requirements and is fit for its intended application. This activity is performed by the Validator.



# 6.3.1.2 ???



The main validation activities are to demonstrate by analysis and/or testing that all the software requirements are specified, implemented, tested and fulfilled as required by the applicable SIL, and to evaluate the safety criticality of all anomalies and non-conformities based on the results of reviews, analyses and tests.



# 6.3.2 Input documents



All system, hardware and software documentation as specified in this European Standard.



# 6.3.3 Output documents



1. Software Validation Plan

2. Software Validation Report

3. Software Validation Verification Report



# 6.3.4 Requirements



# 6.3.4.1 ???



The Software Validation activities shall be developed and performed, with their results evaluated, by a Validator with an appropriate level of independence as defined in 5.1.



# 6.3.4.2 ???



Validation shall be documented with, at least, a Software Validation Plan and a Software Validation Report, as defined in the following.



# 6.3.4.3 ???



A Software Validation Plan shall be written, under the responsibility of the Validator, on the basis of the input documents.



Requirements from 6.3.4.4 to 6.3.4.6 refer to the Software Validation Plan.



# 6.3.4.4 ???



The Software Validation Plan shall include a summary justifying the validation strategy chosen. The justification shall include consideration, according to the required software safety integrity level, of



- a) manual or automated techniques or both,

- b) static or dynamic techniques or both,

- c) analytical or statistical techniques or both,

- d) testing in a real or simulated environment or both.



# 6.3.4.5 ???



The Software Validation Plan shall identify the steps necessary to demonstrate the adequacy of any Software Specification in fulfilling the safety requirements set out in the System Safety Requirements Specification.



# 6.3.4.6 ???



The Software Validation Plan shall identify the steps necessary to demonstrate the adequacy of the Overall Software Test Specification as a test against the Software Requirements Specification.



# 6.3.4.7 ???



A Software Validation Report shall be written, under the responsibility of the Validator, on the basis of the input documents.



Requirements from 6.3.4.8 to 6.3.4.11 refer to the Software Validation Report.



# 6.3.4.8 ???



The results of the validation shall be documented in the Software Validation Report.



# 6.3.4.9 ???



The Validator shall check that the verification process is complete.



# 6.3.4.10 ???



The Software Validation Report shall fully state the software baseline that has been validated.



# 6.3.4.11 ???



The Validation Report shall clearly identify any known deficiencies in the software and the impact these may have on the use of the software.



# 6.3.4.12 ???



A Software Validation Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 6.3.2.



Requirements from 6.3.4.13 to 6.3.4.14 refer to the Software Validation Verification Report.



# 6.3.4.13 ???



Once the Software Validation Plan has been established, verification shall address



- a) that the Software Validation Plan meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 6.3.4.4 to 6.3.4.6,

- b) the internal consistency of the Software Validation Plan.



# 6.3.4.14 ???



Once the Software Validation Report has been established, verification shall address



- a) that the Software Validation Report meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 6.3.4.8 to 6.3.4.11 and 7.7.4.7 to 7.7.4.11,

- b) the internal consistency of the Software Validation Report.



The results shall be recorded in a Software Validation Verification Report.



# 6.3.4.15 ???



The Validator shall be empowered to require or perform additional reviews, analyses and tests.



# 6.3.4.16 ???



The software shall only be released for operation after authorisation by the Validator.



# 6.3.4.17 ???



Simulation and modelling may be used to supplement the validation process.



# 6.4 ???



Software assessment



# 6.4.1 ???



Objective



# 6.4.1.1 ???



To evaluate that the lifecycle processes and their outputs are such that the software is of the defined software safety integrity levels 1-4 and is fit for its intended application.



# 6.4.1.2 ???



For SIL 0 software, requirements of this standard shall be fulfilled but where a certificate stating compliance with EN ISO 9001 is available, no assessment will be required.



# 6.4.2 ???



Input documents



1. System Safety Requirements Specification

2. Software Requirements Specification

3. All other documents necessary to carry out the assessment process.



# 6.4.3 Output documents



1. Software Assessment Plan

2. Software Assessment Report

3. Software Assessment Verification Report



# 6.4.4 Requirements



# 6.4.4.1 ???



The assessment of the software shall be carried out by an Assessor who is independent as described in 5.1.2.6 and 5.1.2.7.



# 6.4.4.2 ???



Software with a Software Assessment Report from another Assessor does not have to be an object of a new assessment. The assessor shall check that the software is fit for its intended use within the intended environment, and that the former assessment stated the software has achieved a safety integrity level at least equal to the required level.



# 6.4.4.3 ???



The Assessor shall have access to all project-related documentation throughout the development process.



# 6.4.4.4 ???



A Software Assessment Plan shall be written, under the responsibility of the Assessor, on the basis of the input documents from 6.4.2. Where appropriate, an existing documented generic Software Assessment Plan or procedure may be used. The requirement in 6.4.4.5 refers to the Software Assessment Plan.



# 6.4.4.5 ???



The Software Assessment Plan shall include the following scope:



- a) aspects with which the assessment deals;

- b) activities throughout the assessment process and their sequential link to engineering activities;

- c) documents to be taken into consideration;

- d) statements on pass/fail criteria and the way to deal with non-conformance cases;

- e) requirements with regard to content and form of the Software Assessment Report.



# 6.4.4.6 ???



A Software Assessment Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 6.4.2.



# 6.4.4.7 ???



Once the Software Assessment Plan has been established, verification shall address:



- a) that the Software Assessment Plan meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 6.4.4.5,

- b) the internal consistency of the Software Assessment Plan.



The results shall be recorded in a Software Assessment Verification Report.



# 6.4.4.8 ???



The Assessor shall assess that the software of the system is fit for its intended purpose and responds correctly to safety issues derived from the System Safety Requirements Specification.



# 6.4.4.9 ???



The Assessor shall assess if an appropriate set of techniques from A, suitable for the intended development, has been selected and applied in accordance to the required safety integrity level.



Moreover, the assessor shall consider the extent to which each technique from A is applied, i.e. whether it is applied to all or to only part of the software, and also look for evidence that it is properly applied.



# 6.4.4.10 ???



The Assessor shall assess the configuration and change management system and the evidences on its use and application.



# 6.4.4.11 ???



The Assessor shall review the evidence of the competency of the project staff according to B and shall assess the organisation for the software development according to 5.1.



# 6.4.4.12 ???



For any software containing safety-related application conditions, the Assessor shall check for noted deviations, non-compliances to requirements and recorded non-conformities if these have an impact on safety, and make a judgment whether the justification from the project is acceptable. The result shall be stated in the assessment report.



# 6.4.4.13 ???



The Assessor shall assess the verification and validation activities and the supporting evidence.



# 6.4.4.14 ???



The Assessor shall agree the scope and contents of the Software Validation Plan. This agreement shall also make a statement concerning the presence of the Assessor during testing.



# 6.4.4.15 ???



The Assessor may carry out audits and inspections (e.g. witnessing tests) throughout the entire development process. The Assessor may ask for additional verification and validation work.



NOTE It is of advantage to involve the Assessor early in the project.



# 6.4.4.16 ???



A Software Assessment Report shall be written under the responsibility of the Assessor. Requirements from 6.4.4.17 to 6.4.4.19 refer to the Software Assessment Report.



# 6.4.4.17 ???



The Software Assessment Report shall meet the requirements of the Software Assessment Plan and provide a conclusion and recommendations.



# 6.4.4.18 ???



The Assessor shall record his/her activities as a consistent base for the Software Assessment Report. These shall be summarised in the Software Assessment report.



# 6.4.4.19 ???



The Assessor shall identify and evaluate any non-conformity with the requirements of this European Standard and judge the impact on the final result. These non-conformities and their judgments shall be listed in the Software Assessment Report.



# 6.5 Software quality assurance



# 6.5.1 Objectives



# 6.5.1.1 ???



To identify, monitor and control all those activities, both technical and managerial, which are necessary to ensure that the software achieves the quality required. This is necessary to provide the required qualitative defence against systematic faults and to ensure that an audit trail can be established to allow verification and validation activities to be undertaken effectively.



# 6.5.1.2 ???



To provide evidence that the above activities have been carried out.



# 6.5.2 Input documents



All the documents available at each stage of the lifecycle.



# 6.5.3 Output documents



1. Software Quality Assurance Plan

2. Software Configuration Management Plan, if not available at system level

3. Software Quality Assurance Verification Report



# 6.5.4 Requirements



# 6.5.4.1 ???



All the plans shall be issued at the beginning of the project and updated during the lifecycle.



# 6.5.4.2 ???



The organisations taking part in the software development shall implement and use a Quality Assurance System compliant with EN ISO 9000, to support the requirements of this European Standard. EN ISO 9001 certification is highly recommended.



# 6.5.4.3 ???



A Software Quality Assurance Plan shall be written, under the responsibility of the Verifier, on the basis of the input documents from 6.5.2.



The requirements from 6.5.4.4 to 6.5.4.6 refer to the Software Quality Assurance Plan.



# 6.5.4.4 ???



A Software Quality Assurance Plan shall be written and shall be specific to the project. It shall implement the requirements of 6.5.4.5.



# 6.5.4.5 ???



As a minimum, the following items shall be specified or referenced in the Software Quality Assurance Plan.



- a) Definition of the life-cycle model:



1. activities and elementary tasks consistent with the plans, e.g. Safety Plan, that have been established at the System level;

2. entry and exit criteria of each activity;

3. inputs and outputs of each activity;

4. major quality activities;

5. the entity responsible for each activity.



- b) Documentation structure.

- c) Documentation control:



1. roles involved for writing, checking and approval;

2. scope of distribution;

3. archiving.



- d) Tracking and tracing of deviations.

- e) Methods, measures and tools for quality assurance according to the allocated safety integrity levels (refer to A).

- f) Justifications, as defined in 4.7 to 4.9, that each combination of techniques or measures selected according to A is appropriate to the defined software safety integrity level.



Some of the Software Quality Assurance Plan required information may be contained in other documents, such as a separate Software Configuration Management Plan, a Maintenance Plan, a Software Verification plan and a Software Validation Plan. The sub-clauses of the Software Quality Assurance Plan shall reference the documents in which the information is contained. In any case the content of each sub-clause of the Software Quality Assurance Plan shall be specified either directly or by reference to another document.



The referenced documents shall be reviewed in order to ensure they provide all the required information and that they fully address the requirements of this European Standard.



# 6.5.4.6 ???



Quality assurance activities, actions, documents, etc. required by all normative sub-clauses of this European Standard shall be specified or referenced in the Software Quality Assurance Plan and tailored to the specific project.



# 6.5.4.7 ???



A Software Quality Assurance Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 6.5.2.



The requirement in 6.5.4.8 refers to the Software Quality Assurance Verification Report.



# 6.5.4.8 ???



Once the Software Quality Assurance Plan has been established, verification shall address



- a) that the Software Quality Assurance Plan meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 6.5.4.4 to 6.5.4.6,

- b) the internal consistency of the Software Quality Assurance Plan.



The results shall be recorded in a Software Quality Assurance Verification Report.



# 6.5.4.9 ???



Each planning document shall have a paragraph specifying details about its own updating throughout the project: frequency, responsibility, method.



# 6.5.4.10 ???



Each software document and deliverable shall be placed under configuration control from the time of its first release.



# 6.5.4.11 ???



Changes to all items under Configuration Management Control shall be authorised and recorded.



# 6.5.4.12 ???



In addition to software development, the Configuration Management System shall also cover the software development environment used during the full lifecycle.



This extension, necessary for the reproducibility of the development and for the maintenance activities, shall include all the tools, translators, data and test files, parameterisation files, and supporting hardware platforms.



# 6.5.4.13 ???



The supplier shall establish, document and maintain procedures for control of the external suppliers, including



- – methods and relevant records to ensure that software provided by external suppliers adheres to established requirements. Previously developed software shall be assured to be compliant with the required software safety integrity level and dependability. New software shall be developed and maintained in conformity with the Software Quality Assurance Plan of the Supplier or with a specific Software Quality Assurance Plan prepared by the external supplier in accordance with the Software Quality Assurance Plan of the Supplier,

- – methods and relevant records to ensure that the requirements provided to the External Supplier are adequate and complete.



# 6.5.4.14 ???



Traceability to requirements shall be an important consideration in the validation of a safety-related system and means shall be provided to allow this to be demonstrated throughout all phases of the lifecycle.



# 6.5.4.15 ???



Within the context of this European Standard, and to a degree appropriate to the specified software safety integrity level, traceability shall particularly address



- a) traceability of requirements to the design or other objects which fulfil them,

- b) traceability of design objects to the implementation objects which instantiate them,

- c) traceability of requirements and design objects to the tests (component, integration, overall test) and analyses that verify them.



Traceability shall be the subject of configuration management.



# 6.5.4.16 ???



In special cases, e.g. pre-existing software or prototyped software, traceability may be established after the implementation and/or documentation of the code, but prior to verification/validation. In these cases, it shall be shown that verification/validation is as effective as it would have been with traceability over all phases.



# 6.5.4.17 ???



Objects of requirements, design or implementation that cannot be adequately traced shall be demonstrated to have no bearing upon the safety or integrity of the system.



# 6.6 Modification and change control



# 6.6.1 Objectives



# 6.6.1.1 ???



To ensure that the software performs as required, preserving the software safety integrity and dependability when modifying the software.



# 6.6.1.2 ???



These objectives are managed by the Configuration Manager.



# 6.6.2 Input documents



1. Software Quality Assurance Plan

2. Software Configuration Management Plan

3. All relevant design, development and analysis documentation

4. Change Requests

5. Change impact analysis and authorisation



# 6.6.3 Output documents



1. All changed input documents

2. Software Change records (see 9.2.4.11)

3. New Configuration records



# 6.6.4 Requirements



# 6.6.4.1 ???



The Change Management Process shall define at least the following aspects:



- a) the documentation needed for problem reporting and/or corrective actions, with the aim of giving feedback to the responsible management;

- b) analysis of the information collected in the problem reports to identify its causes;

- c) the practices to be followed for reporting, tracking and resolving problems identified both during the development phase and during software maintenance;

- d) the specific organisational responsibilities with regard to development and software maintenance;

- e) how to apply controls to ensure that corrective actions are taken and that they are effective;

- f) impact analysis of the effect of the changes on the software component under development or already delivered;

- g) impact analysis shall state the re-verification, re-validation and re-assessment necessary for the change;

- h) where multiple changes are applied, the impact analysis shall consider the cumulative impact;

NOTE Several changes may cumulatively require a complete re-test.

- i) authorisation before implementation.



# 6.6.4.2 ???



All changes shall initiate a return to an appropriate phase of the lifecycle. All subsequent phases shall then be carried out in accordance with the procedures specified for the specific phases in accordance with the requirements in this European Standard.



# 6.7 Support tools and languages



# 6.7.1 Objectives



# 6.7.1.1 ???



The objective is to provide evidence that potential failures of tools do not adversely affect the integrated toolset output in a safety related manner that is undetected by technical and/or organisational measures outside the tool. To this end, software tools are categorised into three classes namely, T1, T2 & T3 respectively (see definitions in 3.1).



When tools are being used as a replacement for manual operations, the evidence of the integrity of tools output can be adduced by the same process steps as if the output was done in manual operation. These process steps might be replaced by alternative methods if an argumentation on the integrity of tools output is given and the integrity level of the software is not decreased by the replacement.



# 6.7.2 Input documents



Tools specification or manual.



# 6.7.3 Output documents



Tools validation report (when needed see 6.7.4.4 or 6.7.4.6).



# 6.7.4 Requirements



# 6.7.4.1 ???



Software tools shall be selected as a coherent part of the software development activities.



NOTE Appropriate tools to support the development of software should be used in order to increase the integrity of the software by reducing the likelihood of introducing or not detecting faults during the development. Examples of tools relevant to the phases of the software development lifecycle include:



- a) transformation or translation tools that convert a software or design representation (e.g. text or a diagram) from one abstraction level to another: design refinement tools, compilers, assemblers, linkers, binders, loaders and code generation tools,

- b) verification and validation tools such as static code analysers, test coverage monitors, theorem proving assistants, simulators and model checkers,

- c) diagnostic tools used to maintain and monitor the software under operating conditions,

- d) infrastructure tools such as development support systems,

- e) configuration control tools such as version control tools,

- f) application data tools that produce or maintain data which are required to define parameters and to instantiate system functions e.g. function parameters, instrument ranges, alarm and trip levels, output states to be adopted at failure, geographical layout.



The selected tools should be able to cooperate. In this context, tools cooperate if the outputs from one tool have suitable content and format for automatic input to a subsequent tool, thus minimizing the possibility of introducing human error in the reworking of intermediate results.



Tools shall be selected and demonstrated to be compatible with the needs of the application. The availability of suitable tools to supply the services that are necessary over the whole lifetime of the software shall be considered.



# 6.7.4.2 ???



The selection of the tools in classes T2 and T3 shall be justified (see 7.3.4.12). The justification shall include the identification of potential failures which can be injected into the tools output and the measures to avoid or handle such failures.



# 6.7.4.3 ???



All tools in classes T2 and T3 shall have a specification or manual which clearly defines the behaviour of the tool and any instructions or constraints on its use.



# 6.7.4.4 ???









necessary for a manual process as a replacement for the tool and an argument presented if these steps are replaced by alternatives (e. g. validation of the tool). Evidence may also be based on



- a suitable combination of history of successful use in similar environments and for similar applications (within the organisation or other organisations),

- tool validation as specified in 6.7.4.5,

- diverse redundant code which allows the detection and control of failures resulting in faults introduced by a tool,

- compliance with the safety integrity levels derived from the risk analysis of the process and procedures including the tools,

- other appropriate methods for avoiding or handling failures introduced by tools.



NOTE 1 A version history may provide assurance of maturity of the tool, and a record of the errors / ambiguities associated with its use in the environment.



NOTE 2 The evidence listed for T3 may also be used for T2 tools in judging the correctness of their results.



# 6.7.4.5 ???



The results of tool validation shall be documented covering the following results:



- a record of the validation activities;

- the version of the tool manual being used;

- the tool functions being validated;

- tools and equipment used;

- the results of the validation activity; the documented results of validation shall state either that the software has passed the validation or the reasons for its failure;

- test cases and their results for subsequent analysis;

- discrepancies between expected and actual results.



# 6.7.4.6 ???



Where the conformance evidence of 6.7.4.4 is unavailable, there shall be effective measures to control failures of the executable safety related software that result from faults that are attributable to the tool.



NOTE 1 An example is the generation of diverse redundant code which allows the detection and control of failures resulting in faults introduced by a translator.



NOTE 2 As an example, the fitness for purpose of a non-trusted compiler can be justified as follows.



The object code produced by the compiler has been subjected to a combination of tests, checks and analyses which are capable of ensuring the correctness of the code to the extent that it is consistent with the target Safety Integrity Level. In particular, the following applies to all tests, checks and analyses.



- Testing has been shown to have a sufficiently high coverage of the implemented code. If there is any code unreachable by testing, it has been shown by checks or analyses that the function concerned is executed correctly when the code is reached on the target.

- Checks and analyses have been applied to the object code and shown to be capable of detecting the types of errors which might result from a defect in the compiler.

- No more translation with the compiler has taken place after testing, checking and analysis.

- If further compilation or translation is carried out, all tests, checks and analyses will be repeated.



# 6.7.4.7 ???



The software or design representation (including a programming language) selected shall



- a) have a translator which has been evaluated for fitness for purpose including, where appropriate, evaluated against the international or national standards,

- b) match the characteristics of the application,

- c) contain features that facilitate the detection of design or programming errors,

- d) support features that match the design method.



A programming language is one of a class of representations of software or design. A Translator converts a software or design representation (e.g. text or a diagram) from one abstraction level to another level. Examples of Translators include: design refinement tools, compilers, assemblers, linkers, binders, loaders and code generation tools.



The evaluation of a Translator may be performed for a specific application project, or for a class of applications. In the latter case all necessary information on the tool regarding the intended and appropriate use of the tool shall be available to the user of the tool. The evaluation of the tool for a specific project may then be reduced to checking general suitability of the tool for the project and compliance to the “specification or manual” (i.e. proper use of the tool). Proper use might include additional verification activities within the specific project.



A validation suite may be used to evaluate the fitness for purpose of a Translator according to defined criteria, which shall include functional and non-functional requirements. For the functional Translator requirements, dynamic testing may be a main validation technique. If possible an automatic testing suite shall be used.



# 6.7.4.8 ???



Where 6.7.4.7 cannot be fully satisfied, the fitness for purpose of the language, and any additional measures which address any identified shortcomings of the language shall be justified and evaluated.



NOTE See NOTE 2 from 6.7.4.6.



# 6.7.4.9 ???



Where automatic code generation or similar automatic translation takes place, the suitability of the automatic Translator for safety-related software development shall be evaluated at the point in the development lifecycle where development support tools are selected.



# 6.7.4.10 ???



Configuration management shall ensure that for tools in classes T2 and T3, only justified versions are used.



# 6.7.4.11 ???



Each new version of a tool that is used shall be justified (see Table 1). This justification may rely on evidence provided for an earlier version if sufficient evidence is provided that



- a) the functional differences (if any) will not affect tool compatibility with the rest of the toolset,

- b) the new version is unlikely to contain significant new, unknown faults.



NOTE Evidence that the new version is unlikely to contain significant new unknown faults may be based on a credible identification of the changes made, and on an analysis of the verification and validation actions performed.



# 6.7.4.12 ???



The relation between the tool classes and the applicable sub-clauses is defined within Table 1.



Table 1 - Relation between tool class and applicable sub-clauses



| Tool class | Applicable sub-clauses                                                                                |

| ---------- | ----------------------------------------------------------------------------------------------------- |

| T1         | 6.7.4.1                                                                                               |

| T2         | 6.7.4.1, 6.7.4.2, 6.7.4.3, 6.7.4.10, 6.7.4.11                                                         |

| T3         | 6.7.4.1, 6.7.4.2, 6.7.4.3, 6.7.4.4, 6.7.4.5 or 6.7.4.6, 6.7.4.7, 6.7.4.8, 6.7.4.9, 6.7.4.10, 6.7.4.11 |



# 7 Generic software development



# 7.1 Lifecycle and documentation for generic software



# 7.1.1 Objectives



# 7.1.1.1 ???



To provide a description of the software itself, from the higher levels of abstraction down to the detailed refinements, in order to create a frame for the demonstration of the achieved safety as well as for future maintenance actions.



# 7.1.2 Requirements



# 7.1.2.1 ???



To the extent required by the software safety integrity level, the documents listed in Table A.1 shall be produced for a generic software.



# 7.1.2.2 ???



The sequence of deliverable documents as they are described in Table A.1 reflects an ideal linear waterfall model. This model is however not intended to be a reference in the sense of schedule and linkage of activities, as it would usually be difficult to achieve a strict compliance in practice. Phases can overlap but verification and validation activities shall demonstrate the consistency of inputs and outputs (documents and software) within and between the phases.



However, the main purpose of the documentation foreseen is to provide a description of the software itself, from the higher levels of abstraction down to the detailed refinements, in order to create a frame for the demonstration of the achieved safety as well as for future maintenance actions.



# 7.2 Software requirements



# 7.2.1 Objectives



# 7.2.1.1 ???



To describe a complete set of requirements for the software meeting all System and Safety Requirements and provide a comprehensive set of documents for each subsequent phase.



# 7.2.1.2 ???



To describe the Overall Software Test Specification.



# 7.2.2 Input documents



1. System Requirements Specification

2. System Safety Requirements Specification

3. System Architecture Description

4. External Interface Specifications (e.g. Software/Software Interface Specification, Software/Hardware Interface Specification)

5. Software Quality Assurance Plan

6. Software Validation Plan



# 7.2.3 Output documents



1. Software Requirements Specification

2. Overall Software Test Specification

3. Software Requirements Verification Report



# 7.2.4 Requirements



# 7.2.4.1 ???



A Software Requirements Specification shall be written, under the responsibility of the Requirements Manager, on the basis of the input documents from 7.2.2.



The requirements from 7.2.4.2 to 7.2.4.15 refer to the Software Requirements Specification.



# 7.2.4.2 ???



The Software Requirements Specification shall express the required properties of the software being developed. These properties, which are all (except safety) defined in ISO/IEC 9126 series, shall include:



- a) functionality (including capacity and response time performance),

- b) robustness and maintainability,

- c) safety (including safety functions and their associated software safety integrity levels),

- d) efficiency,

- e) usability,

- f) portability.



# 7.2.4.3 ???



The software safety integrity level shall be derived as defined in Clause 4 and recorded in the Software Requirements Specification.



# 7.2.4.4 ???



To the extent required by the software safety integrity level, the Software Requirements Specification shall be expressed and structured in such a way that it is:



- a) complete, clear, precise, unequivocal, verifiable, testable, maintainable and feasible,

- b) traceable back to all the input documents.



# 7.2.4.5 ???



The Software Requirements Specification shall include modes of expression and descriptions which are understandable to the responsible personnel involved in the life cycle of the software.



# 7.2.4.6 ???



The Software Requirements Specification shall identify and document all interfaces with any other system, either within or outside the equipment under control, including operators, wherever a direct connection exists or is planned.



# 7.2.4.7 ???



All relevant modes of operation shall be detailed in the Software Requirements Specification.



# 7.2.4.8 ???



All relevant modes of behaviour of the programmable electronics, in particular failure behaviour, shall be documented or referenced (e.g. system level documentation) in the Software Requirements Specification.



# 7.2.4.9 ???



Any constraints between the hardware and the software shall be documented or referenced (e.g. system level documentation) in the Software Requirements Specification.



# 7.2.4.10 ???



To the extent required by the description of system documentation, the Software Requirements Specification shall consider the software self-checking and the hardware checking by the software. Software self-checking consists of the detection and reporting by the software of its own failures and errors.



# 7.2.4.11 ???



The Software Requirements Specification shall include requirements for the periodic testing of functions to the extent required by the System Safety Requirements Specification.



# 7.2.4.12 ???



The Software Requirements Specification shall include requirements to enable all safety functions to be testable during overall system operation to the extent required by the System Safety Requirements Specification.



# 7.2.4.13 ???



All functions to be performed by the software, especially those related to achieving the required system safety integrity level, shall be clearly identified in the Software Requirements Specification.



# 7.2.4.14 ???



Any non-safety functions which the software is required to perform shall be clearly identified in the Software Requirements Specification.



# 7.2.4.15 ???



The Software Requirements Specification shall be supported by techniques and measures from Table A.2. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.2.4.16 ???



An Overall Software Test Specification shall be written, under the responsibility of the Tester, on the basis of the Software Requirements Specification.



The requirements from 7.2.4.17 to 7.2.4.19 refer to the Overall Software Test Specification.



# 7.2.4.17 ???



The Overall Software Test Specification shall be a description of the tests to be performed on the completed software.



# 7.2.4.18 ???



The Overall Software Test Specification shall choose techniques and measures from Table A.7. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.2.4.19 ???



The Overall Software Test Specification shall identify for each required function the test cases including



- a) the required input signals with their sequences and their values,

- b) the anticipated output signals with their sequences and their values,

- c) the test success criteria, including performance and quality aspects.



# 7.2.4.20 ???



A Software Requirements Verification Report shall be written, under the responsibility of the Verifier, on the basis of the System Safety Requirements Specification, Software Requirements Specification, Overall Software Test Specification and Software Quality Assurance Plan.



Requirements from 7.2.4.21 to 7.2.4.22 refer to the Software Requirements Verification Report.



# 7.2.4.21 ???



The Software Requirements Verification Report shall be written in accordance to the generic requirements established for all the Verification Reports (see 6.2.4.13).



# 7.2.4.22 ???



Once the Software Requirements Specification has been established, verification shall address:



- a) the adequacy of the Software Requirements Specification in fulfilling the requirements set out in the System Requirements Specification, the System Safety Requirements Specification and the Software Quality Assurance Plan,

- b) that the Software Requirements Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 7.2.4.2 to 7.2.4.15,

- c) the adequacy of the Overall Software Test Specification as a test against the Software Requirements Specification,

- d) the definition of any additional activity in order to demonstrate the correct coverage of not testable requirements,

- e) the internal consistency of the Software Requirements Specification,

- f) the adequacy of the Software Requirements Specification in fulfilling or taking into account the constraints between hardware and software.



The results shall be recorded in a Software Requirements Verification Report.



# 7.3 Architecture and Design



# 7.3.1 Objectives



# 7.3.1.1 ???



To develop a software architecture that achieves the requirements of the software.



# 7.3.1.2 ???



To identify and evaluate the significance of hardware/software interactions for safety.



# 7.3.1.3 ???



To choose a design method if one has not been previously defined.



# 7.3.1.4 ???



To design software of a defined software safety integrity level from the input documents.



# 7.3.1.5 ???



To ensure that the resultant system and its software will be readily testable from the outset. As verification and test will be a critical element in the validation, particular consideration shall be given to verification and test needs throughout the implementation.



# 7.3.2 Input documents



1. Software Requirements Specification



# 7.3.3 Output documents



1. Software Architecture Specification

2. Software Design Specification

3. Software Interface Specifications












# 7.3.4 Requirements



# 7.3.4.1 ???



A Software Architecture Specification shall be written, under the responsibility of the Designer, on the basis of the Software Requirements Specification.



Requirements from 7.3.4.2 to 7.3.4.14 refer to the Software Architecture Specification.



# 7.3.4.2 ???



The proposed software architecture shall be established and detailed in the Software Architecture Specification.



# 7.3.4.3 ???



The Software Architecture Specification shall consider the feasibility of achieving the Software Requirements Specification at the required software safety integrity level.



NOTE The Software Architecture should minimise the size and complexity of the safety part of the application.



# 7.3.4.4 ???



The Software Architecture Specification shall identify, analyse and detail the significance of all hardware/software interactions.



# 7.3.4.5 ???



The Software Architecture Specification shall identify all software components and for these components identify



- a) whether these components are new or existing,

- b) whether these components have been previously validated and if so their validation conditions,

- c) the software safety integrity level of the component.



# 7.3.4.6 ???



Software components shall



- a) cover a defined subset of software requirements,

- b) be clearly identified and independently versioned inside the configuration management system.



# 7.3.4.7 ???



The use of pre-existing software shall be subject to the following restrictions.



- a) For all software safety integrity levels the following information shall clearly be identified and documented:

- - – the requirements that the pre-existing software is intended to fulfil;

- – the assumptions about the environment of the pre-existing software;

- – interfaces with other parts of the software.



b) For all software safety integrity levels the pre-existing software shall be included in the validation process of the whole software.



- c) For software safety integrity levels SIL 3 or SIL 4, the following precautions shall be taken:



– the verification and validation process shall ensure



1. that the pre-existing software fulfils the allocated requirements,

2. that failures of the pre-existing software are detected and the system where the pre-existing software is integrated into is protected from these failures,

3. that the assumptions about the environment of the pre-existing software are fulfilled.



d) The pre-existing software shall be accompanied by a sufficiently precise (e.g. limited to the used functions) and complete description (i.e. functions, constraints and evidence). The description shall include hardware and/or software constraints of which the integrator shall be aware and take into consideration during application. In particular it forms the vehicle for informing the integrator of what the software was designed for, its properties, behaviour and characteristics.



NOTE Statistical evidence may be used in the validation strategy of the pre-existing software.



# 7.3.4.8 ???



The use of existing verified software components developed according to this European Standard in the design is to be preferred wherever possible.



# 7.3.4.9 ???



Where the software consists of components of different software safety integrity levels then all of the software components shall be treated as belonging to the highest of these levels unless there is evidence of independence between the higher software safety integrity level components and the lower software safety integrity level components. This evidence shall be recorded in the Software Architecture Specification.



# 7.3.4.10 ???



The Software Architecture Specification shall describe the strategy for the software development to the extent required by the software safety integrity level. The Software Architecture Specification shall be expressed and structured in such a way that it is



1. complete, consistent, clear, precise, unequivocal, verifiable, testable, maintainable and feasible,

2. traceable back to the Software Requirements Specification.



# 7.3.4.11 ???



Measures for handling faults shall be included in the Software Architecture Specification in order to achieve the balance between the fault avoidance and fault handling strategies.



# 7.3.4.12 ???



The Software Architecture Specification shall justify that the techniques, measures and tools chosen form a set which satisfies the Software Requirements Specification at the required software safety integrity level.



# 7.3.4.13 ???



The Software Architecture Specification shall take into account the requirements from 8.4.8 when the software is configured by applications data or algorithms.



# 7.3.4.14 ???



The Software Architecture Specification shall choose techniques and measures from Table A.3. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.3.4.15 ???



The size and complexity of the developed software architecture shall be balanced.



# 7.3.4.16 ???



Prototyping may be used in any phase to elicit requirements or to obtain a more detailed view on requirements and their consequences.



# 7.3.4.17 ???



Code from a prototype may be used in the target system only if it is demonstrated that the code and its development and documentation fulfils this European Standard.



# 7.3.4.18 ???



A Software Interface Specification for all Interfaces between the components of the software and the boundary of the overall software shall be written, under the responsibility of the Designer, on the basis of the Software Requirements Specification and the Software Architecture Specification.



The requirement in 7.3.4.19 refers to the Software Interface Specification.



# 7.3.4.19 ???



The description of interfaces shall address



- a) pre/post conditions,

- b) definition and description of all boundary values for all specified data,

- c) behaviour when the boundary value is exceeded,

- d) behaviour when the value is at the boundary,

- e) for time-critical input and output data:

- 1. time constraints and requirements for correct operation,

- 2. management of exceptions.

- f) allocated memory for the interface buffers and the mechanisms to detect that the memory cannot be allocated or all buffers are full, where applicable,

- g) existence of synchronization mechanisms between functions (see e).



All data from and to the interfaces shall be defined for the whole range of values defined by the type of the data, including the ranges which are not used when processed by the functions:



- a) definition and description of all equivalence classes for all specified data and each software function using them,

- b) definition of unused or forbidden equivalence classes.



NOTE The data type includes the following:



- 1. input parameters and output results of functions and/or procedures;

- 2. data specified in telegrams or communication packets;

- 3. data from the hardware.



# 7.3.4.20 ???



A Software Design Specification shall be written, under the responsibility of the Designer, on the basis of the Software Requirements Specification, the Software Architecture Specification and the Software Interface Specification.



Requirements from 7.3.4.21 to 7.3.4.24 refer to the Software Design Specification.



# 7.3.4.21 ???



The input documents shall be available, although not necessarily finalised, prior to the start of the design process.



# 7.3.4.22 ???



The Software Design Specification shall describe the software design based on a decomposition into components with each component having a Software Component Design Specification and a Software Component Test Specification.



# 7.3.4.23 ???



The Software Design Specification shall address



- a) software components traced back to software architecture and their safety integrity level,

- b) interfaces of software components with the environment,

- c) interfaces between the software components,

- d) data structures,

- e) allocation and tracing of requirements on components,

- f) main algorithms and sequencing,

- g) error reporting mechanisms.



# 7.3.4.24 ???



The Software Design Specification shall choose techniques and measures from Table A.4. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.3.4.25 ???



Coding standards shall be developed and specify



- a) good programming practice, as defined by Table A.12,

- b) measures to avoid or detect errors which can be made during application of the language and are not detectable during the verification (see 7.5 and 7.6). Such failures are derived by analysis over all features of the language,

- c) procedures for source code documentation.



# 7.3.4.26 ???



The selection of a coding standard shall be justified to the extent required by the software safety integrity level.



# 7.3.4.27 ???



The coding standards shall be used for the development of all software and be referenced in the Software Quality Assurance Plan.



# 7.3.4.28 ???



In accordance with the required software safety integrity level the design method chosen shall possess features that facilitate



- a) abstraction, modularity and other features which control complexity,

- b) the clear and precise expression of

- - 1. functionality,

- 2. information flow between components,

- 3. sequencing and time related information,

- 4. concurrency,

- 5. data structure and properties,



c) human comprehension,



- d) verification and validation,

- e) software maintenance.



# 7.3.4.29 ???



A Software Integration Test Specification shall be written, under the responsibility of the Integrator, on the basis of the Software Requirements Specification, the Software Architecture Specification, the Software Design Specification and the Software Interface Specifications.



The requirements from 7.3.4.30 to 7.3.4.32 refer to the Software Integration Test Specification.



# 7.3.4.30 ???



The Software Integration Test Specification shall be written in accordance with the generic requirements established for a Test Specification (see 6.1.4.4).



# 7.3.4.31 ???



The Software Integration Test Specification shall address the following:



- a) it shall be shown that each software component provides the specified interfaces for the other components by executing the components together;

- b) it shall be shown that the software behaves in an appropriate manner when the interface is subjected to inputs which are out of specification;

- c) the required input data with their sequences and their values shall be the base of the test cases;

- d) the anticipated output data with their sequences and their values shall be the basis of the test cases;






e) it shall be shown which results of the component test (see 7.5.4.5 and 7.5.4.7) are intended to be reused for the software integration test.



# 7.3.4.32 ???



The Software Integration Test Specification shall choose techniques and measures from Table A.5. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.3.4.33 ???



A Software/Hardware Integration Test Specification shall be written, under the responsibility of the integrator, on the basis of the System Design Description, the Software Requirements Specification, the Software Architecture Specification and the Software Design Specification.



The requirements from 7.3.4.34 to 7.3.4.39 refer to the Software/Hardware Integration Test Specification.



# 7.3.4.34 ???



A Software/Hardware Integration Test Specification should be created early in the development lifecycle, in order that integration testing may be properly directed and that particular design or other integration needs may be suitably provided for. Depending upon the size of the system, the Software/Hardware Integration Test Specification may be subdivided during development into a number of child documents and be naturally added to, as the hardware and software designs evolve and the detailed needs of integration become clearer.



# 7.3.4.35 ???



The Software/Hardware Integration Test Specification shall distinguish between those activities which can be carried out by the supplier on his premises and those that require access to the user's site.



# 7.3.4.36 ???



The Software/Hardware Integration Test Specification shall address the following:



- a) it shall be shown that the software runs in a proper way on the hardware using the hardware via the specified hardware interfaces;

- b) it shall be shown that the software can handle hardware faults as required;

- c) the required timing and performance shall be demonstrated;

- d) the required input data with their sequences and their values shall be the basis of the test cases;

- e) the anticipated output data with their sequences and their values shall be the basis of the test cases;

- f) it shall be shown which results of the component test (see 7.5.4.5) and of the software integration test (see 7.6.4.3) are intended to be reused for the software/hardware integration test.



# 7.3.4.37 ???



The Software/Hardware Integration Test Specification shall document the following:



- a) test cases and test data;

- b) types of tests to be performed;

- c) test environment including tools, support software and configuration description;

- d) test criteria on which the completion of the test will be judged.



# 7.3.4.38 ???



The Software/Hardware Integration Test Specification shall be written in accordance with the generic requirements established for a Test Specification (see 6.1.4.4).



# 7.3.4.39 ???



The Software/Hardware Integration Test Specification shall choose techniques and measures from Table A.5. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.3.4.40 ???



A Software Architecture and Design Verification Report shall be written, under the responsibility of the Verifier, on the basis of the Software Requirements Specification, Software Architecture Specification, Software Design Specification, Software Integration Test Specification and Software/Hardware Integration Test Specification.



The requirements from 7.3.4.41 to 7.3.4.43 refer to the Software Architecture and Design Verification Report.



# 7.3.4.41 ???



The Software Architecture and Design Verification Report shall be written in accordance with the generic requirements established for a Verification Report (see 6.2.4.13).



# 7.3.4.42 ???



After the Software Architecture, Interface and Design Specifications have been established, verification shall address:



- a) the internal consistency of the Software Architecture, Interface and Design Specifications,

- b) the adequacy of the Software Architecture, Interface and Design Specifications in fulfilling the Software Requirements Specification with respect to consistency and completeness,

- c) that the Software Architecture Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.16 as well as the specific requirements in 7.3.4.1 to 7.3.4.14,

- d) that the Software Interface Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.16 as well as the specific requirements in 7.3.4.18 to 7.3.4.19,

- e) that the Software Design Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.16 as well as the specific requirements in 7.3.4.20 to 7.3.4.24,

- f) the adequacy of the Software Architecture Specification and the Software Design Specification in taking into account the hardware and software constraints.



The results shall be recorded in a Software Architecture and Design Verification Report.



# 7.3.4.43 ???



After the Software Integration and Software/Hardware Integration Test Specifications have been established, verification shall address:



- a) that the Software Integration Test Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.16, as well as the specific requirements in 7.3.4.29 to 7.3.4.32,

- b) that the Software/Hardware Integration Test Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.16, as well as the specific requirements in 7.3.4.33 to 7.3.4.39.



The results shall be recorded in a Software Architecture and Design Verification Report.



# 7.4 Component design



# 7.4.1 Objectives



# 7.4.1.1 ???



To develop a software component design that achieves the requirements of the Software Design Specification to the extent required by the software safety integrity level.



# 7.4.1.2 ???



To develop a software component test specification that achieves the requirements of the Software Component Design Specification to the extent required by the software safety integrity level.



# 7.4.2 Input documents



1. Software Design Specification



# 7.4.3 Output documents



1. Software Component Design Specification

2. Software Component Test Specification

3. Software Component Design Verification Report



# 7.4.4 Requirements



# 7.4.4.1 ???



For each component, a Software Component Design Specification shall be written, under the responsibility of the Designer, on the basis of the Software Design Specification.



Requirements from 7.4.4.2 to 7.4.4.6 refer to the Software Component Design Specification.



# 7.4.4.2 ???



For each software component, the following information shall be available:



- author,

- configuration history, and

- short description.



The configuration history shall include a precise identification of the current and all previous versions of the component, specifying the version, date and author, and a description of the changes made from the previous version.



# 7.4.4.3 ???



The Software Component Design Specification shall address:



1. identification of all lowest software units (e.g. subroutines, methods, procedures) traced back to the upper level,

2. their detailed interfaces with the environment and other components with detailed inputs and outputs,

3. their safety integrity level without any further apportionment within the component itself,

4. detailed algorithms and data structures.



Each Software Component Design Specification shall be self consistent and allow transforming into code of the corresponding components.



# 7.4.4.4 ???



Each Software Component Design Specification shall be readable, understandable and testable.



# 7.4.4.5 ???



The size and complexity of each developed Software Component shall be balanced.



# 7.4.4.6 ???



The Software Component Design Specification shall choose techniques and measures from Table A.4. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.4.4.7 ???



For each component, a Software Component Test Specification shall be written, under the responsibility of the Tester, on the basis of the Software Component Design Specification.



The requirements from 7.4.4.8 to 7.4.4.10 refer to the Software Component Test Specification.



# 7.4.4.8 ???



The Software Component Test Specification shall be written in accordance with the generic requirements established for a Test Specification (see 6.1.4.4).



# 7.4.4.9 ???



A Software Component Test Specification shall be produced against which the component shall be tested. These tests shall show that each component performs its intended function. The Software Component Test Specification shall define and justify the required criteria and degree of test coverage to the extent required by the software integrity level. Tests shall be designed so as to fulfil three objectives:



- a) to confirm that the component performs its intended functions (black box testing);

- b) to check how the internal parts of the component interact to carry out the intended functions (black/white box testing);

- c) to confirm that all parts of the component are tested (white box testing).



# 7.4.4.10 ???



The Software Component Test Specification shall choose techniques and measures from Table A.5. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 7.4.4.11 ???



A Software Component Design Verification Report shall be written, under the responsibility of the Verifier, on the basis of the Software Design Specification, Software Component Design Specification and Software Component Test Specification.



# 7.4.4.12 ???



The Software Component Design Verification Report shall be written in accordance with the generic requirements established for a Verification Report (see 6.2.4.13).



# 7.4.4.13 ???



After each Software Component Design Specification has been established, verification shall address:



- a) the adequacy of the Software Component Design Specification in fulfilling the Software Design Specification,

- b) that the Software Component Design Specification meets general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17, as well as the specific requirements in 7.4.4.1 to 7.4.4.6,

- c) the adequacy of the Software Component Test Specification as a set of test cases for the Software Component Design Specification,

- d) that the Software Component Test Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17, as well as the specific requirements in 7.4.4.7 to 7.4.4.10,

- e) the decomposition of the Software Design Specification into software components and the Software Component Design Specification with reference to:



The results shall be recorded in a Software Component Design Verification Report.



# 7.5 Component implementation and testing



# 7.5.1 Objectives



# 7.5.1.1 ???



To achieve software which is analysable, testable, verifiable and maintainable. Component testing is also included in this phase.



# 7.5.2 Input documents



1. Software Component Design Specification

2. Software Component Test Specification



# 7.5.3 Output documents



1. Software Source Code and supporting documentation

2. Software Component Test Report

3. Software Source Code Verification Report



# 7.5.4 Requirements



# 7.5.4.1 ???



The Software Source Code shall be written under the responsibility of the Implementer on the basis of the Software Component Design Specification. Requirements from 7.5.4.2 to 7.5.4.4 refer to the software source code.



# 7.5.4.2 ???



The size and complexity of the developed source code shall be balanced.



# 7.5.4.3 ???



The Software Source Code shall be readable, understandable and testable.



# 7.5.4.4 ???



The Software Source Code shall be placed under configuration control before the commencement of documented testing.



# 7.5.4.5 ???



A Software Component Test Report shall be written, under the responsibility of the Tester, on the basis of the Software Component Test Specification and the Software Source Code.



Requirements from 7.5.4.6 to 7.5.4.7 refer to the Software Component Test Report.



# 7.5.4.6 ???



The Software Component Test Report shall be written in accordance with the generic requirements established for a Test Report (see 6.1.4.5).



# 7.5.4.7 ???



The Software Component Test Report shall include the following features.



- a) A statement of the test results and whether each component has met the requirements of its Software Component Design Specification.

- b) A statement of test coverage shall be provided for each component, showing that the required degree of test coverage has been achieved for all required criteria.



# 7.5.4.8 ???



A Software Source Code Verification Report shall be written, under the responsibility of the verifier, on the basis of the Software Component Design Specification, the Software Component Test Specification and the Software Source Code.



Requirements from 7.5.4.9 to 7.5.4.10 refer to the Software Source Code Verification Report.



# 7.5.4.9 ???



The Software Source Code Verification Report shall be written in accordance with the generic requirements established for a Verification Report (see 6.2.4.13).



# 7.5.4.10 ???



After the Software Source Code and the Software Component Test Report have been established, verification shall address



- a) the adequacy of the Software Source Code as an implementation of the Software Component Design Specification,

- b) the correct use of the chosen techniques and measures from Table A.4 as a set satisfying 4.8 and 4.9,

- c) determining the correct application of the coding standards,

- d) that the Software Source Code meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17, as well as the specific requirements in 7.5.4.1 to 7.5.4.4,

- e) the adequacy of the Software Component Test Report as a record of the tests carried out in accordance with the Software Component Test Specification.



The results shall be recorded in a Software Source Code Verification Report.



# 7.6 Integration



# 7.6.1 Objectives



# 7.6.1.1 ???



To carry out software and software/hardware integration.



# 7.6.1.2 ???



To demonstrate that the software and the hardware interact correctly to perform their intended functions.



# 7.6.2 Input documents



1. Software/Hardware Integration Test Specification

2. Software Integration Test Specification



# 7.6.3 Output documents



1. Software Integration Test Report

2. Software/Hardware Integration Test Report

3. Software Integration Verification Report



# 7.6.4 Requirements



# 7.6.4.1 ???



The integration of software components shall be the process of progressively combining individual and previously tested components into a composite whole in order that the components interfaces and the assembled software may be adequately proven prior to system integration and system test.



# 7.6.4.2 ???



During software/hardware integration any modification or change to the integrated system shall be subject to an impact study which shall identify all components impacted and the necessary reverification activities.



# 7.6.4.3 ???



A Software Integration Test Report shall be written, under the responsibility of the Integrator, on the basis of the Software Integration Test Specification.



Requirements from 7.6.4.4 to 7.6.4.6 refer to the Software Integration Test Report.



# 7.6.4.4 ???



The Software Integration Test Report shall be written in accordance with the generic requirements established for a Test Report (see 6.1.4.5).



# 7.6.4.5 ???



A Software Integration Test Report shall be produced as follows:



- a Software Integration Test Report shall be produced stating the test results and whether the objectives and criteria of the Software Integration Test Specification have been met. If there is a failure, the circumstances for the failure shall be recorded;

- test cases and their results shall be recorded, preferably in machine readable form for subsequent analysis;

- tests shall be repeatable and, if practicable, be performed by automatic means;

- the Software Integration Test Report shall document the identity and configuration of all the items involved.



# 7.6.4.6 ???



The Software Integration Test Report shall demonstrate the correct use of the chosen techniques and measures from Table A.6 as a set satisfying 4.8 and 4.9.



# 7.6.4.7 ???



A Software/Hardware Integration Test Report shall be written, under the responsibility of the integrator, on the basis of the Software/Hardware Integration Test Specification.



Requirements from 7.6.4.8 to 7.6.4.10 refer to the Software/Hardware Integration Test Report.



# 7.6.4.8 ???



The Software/Hardware Integration Test Report shall be written in accordance with the generic requirements established for a Test Report (see 6.1.4.5).



# 7.6.4.9 ???



A Software/Hardware Integration Test Report shall be produced as follows:



- the Software/Hardware Integration Test Report shall state the test results and whether the objectives and criteria of the Software/Hardware Integration Test Specification have been met. If there is a failure, the circumstances of the failure shall be recorded;

- test cases and their results shall be recorded, preferably in a machine-readable form for subsequent analysis;

- the Software/Hardware Integration Test Report shall document the identity and configuration of all items involved.



# 7.6.4.10 ???



The Software/Hardware Integration Test Report shall demonstrate the correct use of the chosen techniques and measures from Table A.6 as a set satisfying 4.8 and 4.9.



# 7.6.4.11 ???



A Software Integration Verification Report shall be written, under the responsibility of the Verifier, on the basis of the Software and Software/Hardware Integration Test Specifications and the corresponding test reports.



Requirements from 7.6.4.12 to 7.6.4.13 refer to the Software Integration Verification Report.



# 7.6.4.12 ???



The Software Integration Verification Report shall be written in accordance with the generic requirements established for a Verification Report (see 6.2.4.13).



# 7.6.4.13 ???



After the Software Integration Test Report and the Software/Hardware Integration Test Report have been established, verification shall address:



- the adequacy of the Software Integration Test Report as a record of the tests carried out in accordance with the Software Integration Test Specification,

- whether the Software Integration Test Report meets the requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17, as well as the specific requirements in 7.6.4.3 to 7.6.4.6.



# 7.7 Overall Software Testing / Final Validation



# 7.7.1 Objectives



# 7.7.1.1 ???



To analyse and test the integrated software and hardware to ensure compliance with the Software Requirements Specification with particular emphasis on the functional and safety aspects according to the software safety integrity level and to check whether it is fit for its intended application.



# 7.7.2 Input documents



1. Software Requirements Specification

2. Overall Software Test Specification

3. Software Verification Plan

4. Software Validation Plan

5. All Hardware and Software Documentation including intermediate verification results

6. System Safety Requirements Specification



# 7.7.3 Output documents



1. Overall Software Test Report

2. Software Validation Report

3. Release Note



# 7.7.4 Requirements



# 7.7.4.1 ???



An Overall Software Test Report shall be written, under the responsibility of the Tester, on the basis of the Overall Software Test Specification.



Requirements from 7.7.4.2 to 7.7.4.4 refer to the Overall Software Test Report.



# 7.7.4.2 ???



The Overall Software Test Report shall be written in accordance with the generic requirements established for a Test Report (see 6.1.4.5).



# 7.7.4.3 ???



The Validator shall specify and perform supplementary tests on his discretion or have them performed by the Tester. While the Overall Software Tests are mainly based on the structure of the Software Requirements Specification, the added value the Validator shall contribute, are tests which stress the system by complex scenarios reflecting the actual needs of the user.



# 7.7.4.4 ???



The results of all tests and analyses shall be recorded in a Overall Software Test Report.



# 7.7.4.5 ???



The software shall be exercised either by connection to real items of hardware or actual systems with which it would interface in operation, or by simulation of input signals and loads driven by outputs. It shall be exercised under conditions present during normal operation, anticipated occurrences and undesired conditions requiring system action. Where simulated inputs or loads are used it shall be shown that these do not differ significantly from the inputs and loads encountered in operation.



NOTE Simulated inputs or loads might replace inputs or loads which are only present at system level or in faulty modes.



# 7.7.4.6 ???



A Software Validation Report shall be written, under the responsibility of the Validator, on the basis of the Software Validation Plan.



Requirements from 7.7.4.7 to 7.7.4.11 refer to the Software Validation Report.



# 7.7.4.7 ???



The Software Validation Report shall be written in accordance with the generic requirements established for the Validation Report (see 6.3.4.7 to 6.3.4.11).



# 7.7.4.8 ???



Once integration is finished and overall software testing and analysis are complete, a Software Validation Report shall be produced as follows:



- a) it shall state whether the objectives and criteria of the Software Validation Plan have been met. Deviations to the plan shall be recorded and justified;

- b) it shall give a summary statement on the tests results and whether the whole software on its target machine fulfils the requirements set out in the Software Requirements Specification;

- c) an evaluation of the test coverage on the requirements of the Software Requirements Specification shall be provided;

- d) an evaluation of other verification activities in accordance to the Software Verification Plan and Report shall be done together with a check that requirements tracing is fully performed and covered;

- e) if the Validator produces own test cases not given to the Tester the Software Validation Report shall document these in accordance with 6.3.4.7 to 6.3.4.11.



# 7.7.4.9 ???



The Software Validation Report shall contain the confirmation that each combination of techniques or measures selected according to A is appropriate to the defined software safety integrity level. It shall contain an evaluation of the overall effectiveness of the combination of techniques and measures adopted, taking account of the size and complexity of the software produced and taking into account the actual results of testing, verification and validation activities.



# 7.7.4.10 ???



The following shall be addressed in the Software Validation Report:



- a) documentation of the identity and configuration of the software;

- b) statement of appropriate identification of technical support software and equipment;

- c) statement of appropriate identification of simulation models used;

- d) statement about the adequacy of the Overall Software Test Specification;

- e) collection and keeping track of any deviations found;

- f) review and evaluation of all deviations in terms of risk (impact);

- g) a statement that the project has performed appropriate handling of corrective actions in accordance with the change management process and procedures and with a clear identification of any discrepancies found;

- h) statement of each restriction given by the deviations in a traceable way;

- i) a conclusion whether the software is fit for its intended application, taking into account the application conditions and constraints.



# 7.7.4.11 ???



Any discrepancies found, including detected errors and non-compliances with this European Standard or with any of the software requirements or plans, as well as constraints and limitations, shall be clearly identified in a separate sub-clause of the Software Validation Report, evaluated regarding the safety integrity level and included in any Release Note which accompanies the delivered software.



# 7.7.4.12 ???



A Release Note which accompanies the delivered software shall include all restrictions in using the software. These restrictions are derived from:



- a) the detected errors,

- b) non-compliances with this European Standard,

- c) degree of fulfilment of the requirements,

- d) degree of fulfilment of any plan.



# 8 Development of application data or algorithms: systems configured by application data or algorithms



# 8.1 Objectives



# 8.1.1 ???



A characteristic feature in many railway systems is the need to design each installation to meet the individual requirements for a specific application. A system configured by application data and/or by application algorithms allows approved generic software to be customised with the individual requirements for each specific application.



The objective for the development of application data is the correct deriving of the data from the given installation and the check of the intended behaviour, followed by an assessment of the used development process for that application data.



The requirements for the development of application algorithms are the same as the development of generic software as described in Clauses 1-7 and 9.



A typical example is a system whose generic software is pre-configured for a generic railway application by a set of application algorithms, and which is then further configured to each specific installation by instantiation and interconnection of the application algorithms and by a set of configuration data. For instance, the signalling principles of an interlocking system (e.g. signal management, point management) may be implemented by a set of application algorithms.



Application data typically take the form of parameter values or descriptions (identity, type, location, etc.) of external objects. Application algorithms may take the form of e.g. function block diagrams, state charts and relay ladder diagrams, which determine the desired response of the system according to its inputs, its current state and specific parameter values. Application algorithms include logical connections and operations to be executed.



The application data/algorithms are usually produced using dedicated tools. They may be expressed in tabular or diagrammatic formats, which can be interpreted or compiled into executable codes often after conversion into source codes handled via specialised languages (with syntax and semantics).



The customisation of systems through configurability gives the designer different degrees of control over the detailed software functionality.



# 8.1.2 ???



The procedures and the tools used for their development shall be appropriate to the system safety integrity level as determined by the function for which they are developed.



# 8.1.3 ???



The sub-clauses below describe the requirements for the initial development of a configurable system and for the subsequent development of each set of application-specific data/algorithms.



# 8.2 Input documents



1. Software Requirements Specification of generic software

2. Software Architecture Specification of generic software

3. Application conditions of the generic software and application tools

4. User manuals of the generic software and application tools



# 8.3 Output documents



1. Application Preparation Plan

2. Application Requirements Specification

3. Application Architecture and Design

4. Application Test Specification

5. Application Test Report

6. Application Preparation Verification Report

7. Source Code of Application Data/Algorithms

8. Application Data/Algorithms Verification Report



# 8.4 Requirements



# 8.4.1 Application Development Process



# 8.4.1.1 ???



An Application Preparation Plan shall be written, under the responsibility of the Requirements Manager or Designer, on the basis of the input documents from 8.2.



The requirements from 8.4.1.2 to 8.4.1.11 refer to the Application Preparation Plan.



# 8.4.1.2 ???



An Application Preparation Plan shall be produced in order to define and detail the application development process, including all the activities, deliverables and roles in charge of them. It can be produced either for each specific application or for a class of specific applications, i.e. for a generic application.



# 8.4.1.3 ???



The Application Preparation Plan shall define a documentation structure for the application preparation process.



# 8.4.1.4 ???



The Application Preparation Plan shall choose techniques and measures from Table A.11. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 8.4.1.5 ???



The Application Preparation Plan shall specify the procedures and application tools (with their classification based on 6.7) to be used in the application development process.



# 8.4.1.6 ???



The Application Preparation Plan shall include verification and validation activities to ensure that the application data/algorithms are complete, correct and compatible with each other and with the generic application, and to provide evidence that the application conditions of the generic application are met. These verification and validation activities and evidence can be replaced by verification and validation performed on the tools that produce the application data/algorithms. The results are gathered together in the Application Preparation Verification Report and the Application Test Report.



# 8.4.1.7 ???



The Application Preparation Plan shall include verification and validation activities to ensure that the application tools and the generic software are compatible with each other and with the specific application, and to provide evidence that their application conditions are met.



# 8.4.1.8 ???



A risk analysis shall be carried out covering the application development process, including the application tools and procedures, in order to validate the Application Preparation Plan and to meet the required software safety integrity level. The Application Preparation Plan shall include the risk analysis.



# 8.4.1.9 ???



The Application Preparation Plan shall specify the requirements for the independence between staff carrying out verification, validation and preparation tasks according to 5.1.



NOTE Data preparation activities are carried out by application designers.



# 8.4.1.10 ???



The Application Preparation Plan shall define a tool class for any hardware or software tools used in the application preparation lifecycle.



# 8.4.1.11 ???



Where possible, the Application Preparation Plan shall call for notations for specifying requirements and design which are familiar to applications engineers. Where new notations are introduced, the necessary user documentation shall be provided, as well as training where appropriate.



# 8.4.1.12 ???



An Application Data/Algorithms Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 8.2.



The requirement in 8.4.1.13 refers to the Application Data/Algorithms Verification Report.



# 8.4.1.13 ???



Once the Application Preparation Plan has been established, verification shall address:



- a) that the Application Preparation Plan meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 8.4.1.2 to 8.4.1.11,

- b) the internal consistency of the Application Preparation Plan.



The results shall be recorded in an Application Data/Algorithms Verification Report.



# 8.4.1.14 ???



The implementation of the Application Preparation Plan shall be verified and validated for each specific application.



# 8.4.2 ???



# Application Requirements Specification



# 8.4.2.1 ???



An Application Requirements Specification shall be written, under the responsibility of the Requirements Manager, on the basis of the input documents from 8.2.



The requirements from 8.4.2.2 to 8.4.2.3 refer to the Application Requirements Specification.






# 8.4.2.2 ???



The requirements for the specific application shall include the requirements which are specific to the installation under consideration (e.g. track layout, signal locations, speed limits for a signalling system), as well as a recap or reference to the application conditions of the generic software and the application tools, and the standards with which the application shall comply (e.g. signalling principles for a signalling system).



# 8.4.2.3 ???



The requirements related to the application data and algorithms processed by the generic software of the system shall be specified at this stage.



# 8.4.2.4 ???



An Application Data/Algorithms Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 8.2.



The requirement in 8.4.2.5 refers to the Application Data/Algorithms Verification Report.



# 8.4.2.5 ???



Once the Application Requirements Specification has been established, verification shall address



- a) that the Application Requirements Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 8.4.2.2 to 8.4.2.3,

- b) the internal consistency of the Application Requirements Specification.



The results shall be recorded in an Application Data/Algorithms Verification Report.



# 8.4.3 Architecture and Design



The quantity and type of the generic hardware and software components to be used in the specific application shall be specified. The location of components, application data and algorithms in the specific application architecture shall be defined. The application data and algorithms processed by the generic software shall be designed at this stage.



# 8.4.4 Application Data/Algorithms Production



# 8.4.4.1 ???



The application development process shall include the production and compilation of the source code of the generic and specific data/algorithms, as well as verification and testing activities related to this production. The use of diagrammatic languages is recommended for producing the source code of application algorithms. Refer to the Table A.16.



# 8.4.4.2 ???



An Application Test Report shall be written, under the responsibility of the Tester, on the basis of the input documents from 8.2.



The requirement in 8.4.4.3 refers to the Application Test Report.



# 8.4.4.3 ???



The Application Test Report shall document the correct and complete execution of the tests defined in Application Test Specification.



# 8.4.4.4 ???



The Application Preparation Verification Report shall



- a) document every activity performed to ensure correctness and completeness of data/algorithm and their coherency with application principles and specific application architecture,

- b) evaluate compatibility of data/algorithms with generic application.



# 8.4.4.5 ???



An Application Test Specification shall be written, under the responsibility of the Tester, on the basis of the input documents from 8.2.



The requirement in 8.4.4.6 refers to the Application Test Specification.






# 8.4.4.6 ???



The Application Test Specification shall specify tests to be carried out at intermediate or final stage of data/algorithms preparation, in order to ensure



- a) coherency and completeness of data/algorithms with respect to application principles,

- b) coherency and completeness of data/algorithms with respect to specific application architecture.



# 8.4.4.7 ???



An Application Data/Algorithms Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 8.2.



The requirement in 8.4.4.8 refers to the Application Data/Algorithms Verification Report.



# 8.4.4.8 ???



Once the Application Test Specification has been established, verification shall address



- a) that the Application Test Specification meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 8.4.4.6,

- b) the internal consistency of the Application Test Specification.



The results shall be recorded in an Application Data/Algorithms Verification Report.



# 8.4.5 Application Integration and Testing Acceptance



# 8.4.5.1 ???



For some systems the application data/algorithms can be integrated with the generic hardware and software for a factory test before installation on the target system. This may not be necessary where a sufficient degree of confidence can be obtained by other means. The application shall then be installed on the target system, and integration tests within the complete installation shall be carried out. Finally the target system shall be commissioned as a fully operational system, and a final acceptance process of the target system in the complete installation shall be carried out. The Application Test Report shall document the correct and complete execution of tests defined in the Application Test Specification. The Application Preparation Verification Report shall check the completeness and correctness of tests performed on the complete installation.



# 8.4.5.2 ???



An Application Test Specification shall be written, under the responsibility of the Tester, on the basis of the input documents from 8.2.



The requirement in 8.4.5.3 refers to the Application Test Specification.



# 8.4.5.3 ???



The Application Test Specification shall specify tests to be carried out to ensure



- a) correct integration of data/algorithms on generic hardware and software, if needed,

- b) correct integration of data/algorithms with complete installation.



# 8.4.5.4 ???



An Application Data/Algorithms Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 8.2.



The requirement in 8.4.5.5 refers to the Application Data/Algorithms Verification Report.



# 8.4.5.5 ???



Once the Application Test Specification has been established, verification shall address that the Application Test Specification meets the specific requirements in 8.4.5.3.



# 8.4.6 Application Validation and Assessment



Validation and assessment activities shall audit the performance of each stage of the life-cycle.



# 8.4.7 Application preparation procedures and tools



# 8.4.7.1 ???



For each new type of system configured by application data/algorithms, specific procedures and tools shall be developed to allow the application development process specified in 8.4.1 to be applied to installations of the new system. Development of these tools shall be carried out in accordance with this European Standard in parallel with the generic software and hardware for the system. The verification, validation and assessment activities shall ensure that the data preparation tools and the generic software are compatible.



# 8.4.7.2 ???



Any compilation process shall be validated and assessed. It shall be noted that specialised compilers are usually necessary for the data and algorithm conversion.



# 8.4.7.3 ???



All application data/algorithms and associated documentation for each specific application shall be subject to the software deployment requirements as specified in 9.1.



# 8.4.7.4 ???



All application data/algorithms and associated documentation shall be subject to the software maintenance requirements specified in 9.2.



# 8.4.7.5 ???



All application data/algorithms and associated documentation shall be placed under configuration management according to the requirements specified in 6.5 and 6.7. The configuration management of application data/algorithms can be separate from the generic software part.



# 8.4.7.6 ???



The Application Verification Report demonstrate the coverage and enforcement of the application conditions of the generic software and application tools.



# 8.4.8 Development of Generic Software



# 8.4.8.1 ???



Development of the generic software, which supports the execution of application data/algorithms, shall comply with the requirements in 7.1 to 7.7 of this European Standard. The following additional requirements shall also be observed.



# 8.4.8.2 ???



The types or classes of function which can be configured by application data/algorithms in each system and subsystem shall be identified in the Software Requirements Specification documents of the generic software. The safety integrity level allocated to functions will determine the standards to be applied to the subsequent development of the application data/ algorithms for all installations of the system.



# 8.4.8.3 ???



During the design of the generic software the detailed interfaces between the generic software and the application data/algorithms shall be specified, unless this has already been specified at an earlier phase of the lifecycle, for example as a result of a requirement to use an existing application-specific language.



# 8.4.8.4 ???



A rigid separation between the generic software and the application data/algorithms shall be enforced, i.e. it shall be possible to recompile and update either the generic software or the application data/algorithms without needing to update the other, unless there has been a change to the defined interface between the generic software and the application data/algorithms. Likewise, the applications specific data/algorithms shall be separated from the application-generic data/algorithms.



# 8.4.8.5 ???



The change control procedures shall ensure that any amendment to the generic software may only be installed after it has been established that either the revised software is compatible with the original application data/algorithms or the application data/algorithms have been revised.



# 8.4.8.6 ???



Care shall be taken in the verification process and validation test phase of the generic software in order to assure that all relevant combinations of data and algorithms are considered.



If all relevant combinations of data and algorithms have not been considered in the verification, testing and validation process of the generic software, it shall be clearly identified as a limit of use of the generic software. A complement to verification, testing and validation process of the generic software shall be performed when some data or algorithms are defined beyond this limit.



# 8.4.8.7 ???



The generic software shall be designed to detect corrupted application data/algorithms where this is feasible.



# 8.4.8.8 ???



The designers shall publish the Release Note of the generic software and application tools by the Overall Software Testing/Final Validation phase of the generic software and application tools. The contents of these documents shall be subject to verification and validation activities.



The following topics shall be addressed in the document “Application conditions of the generic software and application tools”:



1. references to the user manuals of the generic software and application tools;

2. any constraints on the application data/algorithms e.g. imposed architecture or coding rules to meet the safety integrity levels.



# 9 Software deployment and maintenance



# 9.1 Software deployment



# 9.1.1 Objective



# 9.1.1.1 ???



To ensure that the software performs as required, preserving the required software safety integrity level and dependability when it is deployed in the final environment of application.



# 9.1.2 Input documents



All design, development and analysis documents relevant to the deployment.



# 9.1.3 Output documents



1. Software Release and Deployment Plan

2. Software Deployment Manual

3. Release Notes

4. Deployment Records

5. Deployment Verification Report



# 9.1.4 Requirements



# 9.1.4.1 ???



The deployment shall be carried out under the responsibility of the project manager.



# 9.1.4.2 ???



Before delivering a software release, the software baseline shall be recorded and kept traceable under configuration management control. Pre-existing software and software developed according to a previous version of this European Standard shall also be included.



# 9.1.4.3 ???



The software release shall be reproducible throughout the baseline lifecycle.



# 9.1.4.4 ???



A Release Note shall be written, under the responsibility of the Designer, on the basis of the input documents from 9.1.2.



The requirement in 9.1.4.5 refers to the Release Note.



# 9.1.4.5 ???



A Release Note shall be provided that defines



- the application conditions which shall be adhered to,






b) information of compatibility among software components and between software and hardware,



c) all restrictions in using the software (see 7.7.4.12).



# 9.1.4.6 ???



A Software Deployment Manual shall be written on the basis of the input documents from 9.1.2.



# 9.1.4.7 ???



The Software Deployment Manual shall define procedures in order to correctly identify and install a software release.



# 9.1.4.8 ???



In case of incremental deployment (i.e., deployment of single components), it is highly recommended for SIL 3 and SIL 4, and recommended for SIL 1 and SIL 2, that the software is designed to include facilities which assure that activation of incompatible versions of software components is excluded.



# 9.1.4.9 ???



Configuration management shall ensure that no harm results from the co-presence of different versions of the same software components where it cannot be avoided.



# 9.1.4.10 ???



A rollback procedure (i.e., capability to return to the previous release) shall be available when installing a new software release.



# 9.1.4.11 ???



The software shall have embedded self-identification mechanisms, allowing its identification at the loading process and after loading into the target. The self-identification mechanism should indicate version information for the software and any configuration data as well as the product identity.



NOTE The data within the code, containing the information about the software release, is recommended to be protected through coding (see Table A.3 “Error Detecting Codes”).



# 9.1.4.12 ???



A Deployment Record shall be written on the basis of the input documents from 9.1.2.



# 9.1.4.13 ???



A Deployment Record shall give evidence that intended software has been loaded, by inspection of the embedded self-identification mechanisms (see 9.1.4.11). This record shall be stored among the delivered system related documents like other verifications and is part of the commissioning and acceptance.



# 9.1.4.14 ???



The deployed software shall be traceable to delivered installations.



NOTE This is of special importance when critical faults are discovered and need to be corrected in more than one installation.



# 9.1.4.15 ???



Diagnostic information shall be provided by the software, as part of fault monitoring.



# 9.1.4.16 ???



A Deployment Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 9.1.2.



# 9.1.4.17 ???



Once the Software Deployment Manual has been established, verification shall address



a) that the Software Deployment Manual meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 9.1.4.7,



b) the internal consistency of the Software Deployment Manual.



# 9.1.4.18 ???



Once the Deployment Record has been established, verification shall address



a) that the Deployment Record meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 9.1.4.13,



b) the internal consistency of the Deployment Record.



# 9.1.4.19 ???



Once the Release Note has been established, verification shall address



- a) that the Release Note meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 9.1.4.5,

- b) the internal consistency of the Release Note.



The results shall be recorded in a Deployment Verification Report.



# 9.1.4.20 ???



Measures shall be included in the software package to prevent or detect errors occurring during storage, transfer, transmission or duplication of executable code or data. The executable code is recommended to be coded (see Table A.3 “Error Detecting Codes”) as part of checking the integrity of the code in the load process.



# 9.2 Software maintenance



# 9.2.1 Objective



# 9.2.1.1 ???



To ensure that the software performs as required, preserving the required software safety integrity level and dependability when making corrections, enhancements or adaptations to the software itself. See also 6.6 “Modification and change control” of this European Standard and phase 13 “Modification and retrofit” in EN 50126-1.



# 9.2.2 Input documents



All relevant design, development and analysis documents



# 9.2.3 Output documents



1. Software Maintenance Plan

2. Software Change Records

3. Software Maintenance Records

4. Software Maintenance Verification Report



# 9.2.4 Requirements



# 9.2.4.1 ???



Although this European Standard is not intended to be retrospective, applying primarily to new developments and only applying in its entirety to existing software if these are subjected to major modifications, 9.2 concerning software maintenance applies to all changes, even those of a minor nature. However, application of the whole this European Standard during upgrades and maintenance of existing software is highly recommended.



# 9.2.4.2 ???



For any software safety integrity level, the supplier shall, before starting work on any change, decide whether the maintenance actions are to be considered as major or minor or whether the existing maintenance methods for the system are adequate. The decision shall be justified and recorded by the supplier and shall be submitted to the Assessor’s evaluation.



# 9.2.4.3 ???



Maintenance shall be carried out in accordance with the guidelines contained in ISO/IEC 90003.



# 9.2.4.4 ???



Maintainability shall be designed as an inherent aspect of the software, in particular by following the requirements of 7.3, 7.4 and 7.5. ISO/IEC 9126 series shall also be employed in order to implement and verify a minimum level of maintainability.



# 9.2.4.5 ???



A Software Maintenance Plan shall be written on the basis of the input documents from 9.2.2.



The requirement 9.2.4.6 refers to the Software Maintenance Plan.



# 9.2.4.6 ???



Procedures for the maintenance of software shall be established and recorded in the Software Maintenance Plan. These procedures shall also address



- a) control of error reporting, error logs, maintenance records, change authorisation and software/system configuration and the techniques and measures in Table A.10,

- b) verification, validation and assessment of any modification,

- c) definition of the Authority which approves the changed software, and

- d) authorisation for the modification.



# 9.2.4.7 ???



A Software Maintenance Record shall be written on the basis of the input documents from 9.2.2.



The requirement in 9.2.4.8 refers to the Software Maintenance Record.



# 9.2.4.8 ???



A Software Maintenance Record shall be established for each Software Item before its first release, and it shall be maintained. In addition to the requirements of ISO/IEC 90003:2004 for _Maintenance Records and Reports_ (see ISO/IEC 90003:2004, section “Maintenance”), this Record shall also include



- a) references to all the Software Change Records for that software item,

- b) change impact assessment,

- c) test cases for components, including revalidation and regression testing data, and

- d) software configuration history.



# 9.2.4.9 ???



A Software Change Record shall be written on the basis of the input documents from 9.2.2.



The requirement in 9.2.4.10 refers to the Software Change Record.



# 9.2.4.10 ???



A Software Change Record shall be established for each maintenance activity. This record shall include



- a) the modification or change request, version, nature of fault, required change and source for change,

- b) an analysis of the impact of the maintenance activity on the overall system, including hardware, software, human interaction and the environment and possible interactions,

- c) the detailed specification of the modification or change carried out, and

- d) revalidation, regression testing and re-assessment of the modification or change to the extent required by the software safety integrity level. The responsibility for revalidation can vary from project to project, according to the software safety integrity level. Also the impact of the modification or change on the process of revalidation can be confined to different system levels (only changed components, all identified affected components, the complete system). Therefore the Software Validation Plan shall address both problems, according to the software safety integrity level. The degree of independence of revalidation shall be the same as that for validation.



# 9.2.4.11 ???



A Software Maintenance Verification Report shall be written, under the responsibility of the Verifier, on the basis of the input documents from 9.2.2.



Requirements from 9.2.4.12 to 9.2.4.14 refer to the Software Maintenance Verification Report.



# 9.2.4.12 ???



Once the Software Maintenance Plan has been established, verification shall address



- a) that the Software Maintenance Plan meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 9.2.4.6,

- b) the internal consistency of the Software Maintenance Plan.



# 9.2.4.13 ???



Once the Software Maintenance Record has been established, verification shall address



- a) that the Software Maintenance Record meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 9.2.4.8,

- b) the internal consistency of the Software Maintenance Record.



# 9.2.4.14 ???



Once the Software Change Record has been established, verification shall address



- a) that the Software Change Record meets the general requirements for readability and traceability in 5.3.2.7 to 5.3.2.10 and in 6.5.4.14 to 6.5.4.17 as well as the specific requirements in 9.2.4.10,

- b) the internal consistency of the Software Change Record.



# 9.2.4.15 ???



The maintenance activities shall be carried out following the Software Maintenance Plan.



# 9.2.4.16 ???



The techniques and measures from Table A.10 shall be chosen. The selected combination shall be justified as a set satisfying 4.8 and 4.9.



# 9.2.4.17 ???



Maintenance shall be performed with at least the same level of expertise, tools, documentation, planning and management as for the initial development of the software. This shall apply also to configuration management, change control, document control, and independence of involved parties.



# 9.2.4.18 ???



External supplier control, problem reporting and corrective actions shall be managed with the same criteria specified in the relevant paragraphs of the Software Quality Assurance (6.5) as for new software development.



# 9.2.4.19 ???



For each reported problem or enhancement a safety impact analysis shall be made.



# 9.2.4.20 ???



For software under maintenance, mitigation actions proportionate to the identified risk shall be taken in order to ensure the overall integrity of the system whilst the reported problems are investigated and corrected.



