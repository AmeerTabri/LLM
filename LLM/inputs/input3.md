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

Figure 1 — Overview of the ISO 26262 series of standards

# 1 Scope

This document is intended to be applied to safety-related systems that include one or more electrical and/or electronic (E/E) systems and that are installed in series production road vehicles, excluding mopeds. This document does not address unique E/E systems in special vehicles such as E/E systems designed for drivers with disabilities.

NOTE Other dedicated application-specific safety standards exist and can complement the ISO 26262 series of standards or vice versa.

Systems and their components released for production, or systems and their components already under development prior to the publication date of this document, are exempted from the scope of this edition. For further development or alterations based on systems and their components released for production prior to the publication of this document, only the modifications will be developed in accordance with this document. This document addresses integration of existing systems not developed according to this document and systems developed according to this document by tailoring the safety lifecycle.

This document addresses possible hazards caused by malfunctioning behaviour of safety-related E/E systems, including interaction of these systems. It does not address hazards related to electric shock, fire, smoke, heat, radiation, toxicity, flammability, reactivity, corrosion, release of energy and similar hazards, unless directly caused by malfunctioning behaviour of safety-related E/E systems.

This document describes a framework for functional safety to assist the development of safety-related E/E systems. This framework is intended to be used to integrate functional safety activities into a company-specific development framework. Some requirements have a clear technical focus to implement functional safety into a product; others address the development process and can therefore be seen as process requirements in order to demonstrate the capability of an organization with respect to functional safety.

This document does not address the nominal performance of E/E systems.

This document provides an overview of the ISO 26262 series of standards, as well as giving additional explanations, and is intended to enhance the understanding of the other parts of the ISO 26262 series of standards. It has an informative character only and describes the general concepts of the ISO 26262 series of standards in order to facilitate comprehension. The explanation expands from general concepts to specific contents.

In the case of inconsistencies between this document and another part of the ISO 26262 series of standards, the requirements, recommendations and information specified in the other part of the ISO 26262 series of standards apply.

# 2 Normative references

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

ISO 26262-1, Road vehicles — Functional safety — Part 1: Vocabulary

# 3 Terms and definitions

For the purposes of this document, the terms, definitions and abbreviated terms given in ISO 26262-1 apply.

ISO and IEC maintain terminological databases for use in standardization at the following addresses:

- IEC Electropedia: available at http://www.electropedia.org/
- ISO Online browsing platform: available at https://www.iso.org/obp

# 4 Key concepts of ISO 26262

# 4.1 Functional safety for automotive systems (relationship with IEC 61508[1])

IEC 61508, Functional Safety of electrical/electronic/programmable electronic safety-related systems, is designated by IEC as a generic standard and a basic safety publication. This means that industry sectors will base their own standards for functional safety on the requirements of IEC 61508.

In the automotive industry, there are a number of issues with applying IEC 61508 directly. Some of these issues and corresponding differences in the ISO 26262 series of standards are described below.

IEC 61508 is based upon the model of “equipment under control”, for example an industrial plant that has an associated control system as follows:

1. A hazard analysis identifies the hazards associated with the equipment under control (including the equipment control system), to which risk reduction measures will be applied. This can be achieved through electrical/electronic/programmable electronic (E/E/PE) systems, or other technology safety-related systems (e.g. a safety valve), or external measures (e.g. a physical containment of the plant). The ISO 26262 series of standards contains a normative automotive scheme for hazard classification based on severity, probability of exposure and controllability.
2. Risk reduction allocated to E/E/PE electronic systems is achieved through safety functions, which are designated as such. These safety functions are either part of a separate protection system, or can be incorporated into the plant control. It is not always possible to make this distinction in automotive systems. The safety of a vehicle depends on the behaviour of the control systems themselves.

The ISO 26262 series of standards uses the notion of safety goals and a safety concept as follows:

- a hazard analysis and risk assessment identifies hazards and hazardous events that need to be prevented, mitigated, or controlled;
- at least one safety goal is associated with each hazardous event that has been classified as ASIL A, B, C or D;
- an Automotive Safety Integrity Level (ASIL) is associated with each safety goal;
- the functional safety concept is a statement of the functionality to achieve the safety goal(s);
- the technical safety concept is a statement of how this functionality is implemented on the system level by hardware and software;
- software safety requirements and hardware safety requirements state the specific safety requirements which will be implemented as part of the software and hardware design.

EXAMPLE The airbag system.

- One of the hazards is unintended deployment.
- An associated safety goal is that the airbag only deploys when a crash occurs that requires the deployment.

— The functional safety concept can specify a redundant function to detect whether the vehicle is in a collision.

— The technical safety concept can specify the implementation of two independent accelerometers with different axial orientations and two independent firing circuits. The squib deploys if both are closed.

IEC 61508 is aimed at singular or low volume systems. The system is built and tested, then installed in the plant, and then safety validation is performed. For mass-market systems such as road vehicles, safety validation is performed before the release for volume (series) production. Therefore, the order of lifecycle activities in the ISO 26262 series of standards is different. Related to this, ISO 26262-7 addresses requirements for production. These are not covered in IEC 61508.

IEC 61508 does not address specific requirements for managing development across multiple organizations and supply chains. Because automotive systems are produced by vehicle manufacturers themselves, by one or more suppliers to the manufacturer or by collaboration between manufacturer and supplier(s), the ISO 26262 series of standards includes requirements to explicitly address this issue, including the Development Interface Agreement (DIA) (see ISO 26262-8:2018, Clause 5).

IEC 61508 does not contain normative requirements for hazard classification. The ISO 26262 series of standards contains an automotive scheme for hazard classification. This scheme recognises that a hazard in an automotive system does not necessarily lead to an accident. The outcome will depend on whether the persons at risk are actually exposed to the hazard in the situation in which it occurs; and whether the involved people are able to take steps to control the outcome of the hazard. An example of this concept, applied to a failure which affects the controllability of a moving vehicle, is given in Figure 2.

NOTE This concept is intended only to demonstrate that there is not necessarily a direct correlation between a failure occurring and the accident. It is not a representation of the hazard analysis and risk assessment process, although the parameters evaluated in this process are related to the probabilities of the state transitions shown in the figure.

Figure 2 — State machine model of automotive risk

The requirements for hardware development (ISO 26262-5) and software development (ISO 26262-6) are adapted for the state-of-the-art in the automotive industry. For the methods listed in the ISO 26262 series of standards specific goals are provided. To achieve these goals, the provided methods can be applied or a rationale that alternative methods can also achieve the goal is provided.

Safety requirements in the ISO 26262 series of standards are assigned an ASIL (Automotive Safety Integrity Level) rather than a SIL (Safety Integrity Level). The main motivation for this is that the SIL in IEC 61508 is stated in probabilistic terms (see IEC 61508-1:2010, Table 3). IEC 61508 acknowledges that qualitative judgement is often required in respect of systematic safety integrity while requiring quantitative techniques for hardware safety integrity. An ASIL in ISO 26262 is primarily concerned with requirements for achieving systematic safety in the system, hardware and software; however, there are probabilistic targets associated with compliance to the requirements of an ASIL with respect to random hardware failures.

# 4.2 Item, system, element, component, hardware part and software unit

The terms item, system, element, component, hardware part and software unit are defined in ISO 26262-1:2018. Figure 3 shows the relationship of item, system, component, hardware part and software unit. Figure 4 shows an example of item dissolution. A divisible element can be labelled as a system or a component. A divisible element that meets the criteria of a system can be labelled as a system. A component is a non-system level, logically and technically separable element. Often the term component is applied to an element that is only comprised of parts and units, but can also be applied to an element comprised of lower-level elements from a specific technology area e.g. electrical / electronic technology (see Figure 4). A hardware part can be further hierarchically composed of hardware subparts and hardware elementary subparts as applicable.

NOTE 1 Depending on the context, the term “element” can apply to the entities “system”, “component”, “hardware part” and “software unit” in this chart, according to ISO 26262-1:2018, 3.41.

NOTE 2 The system, as it is defined in ISO 26262-1, is at least a sensor, a controller, and an actuator (e.g. at least 3 related elements).

NOTE 3 \*means N are possible.

Figure 3 — Relationship of item, system, component, hardware part and software unit

Figure 4 — Example item dissolution

# 4.3 Relationship between faults, errors and failures

# 4.3.1 Progression of faults to errors to failures

The terms fault, error and failure are defined in ISO 26262-1:2018. Figure 5 depicts the progression of faults to errors to failures from three different types of causes: systematic software issues, random hardware issues and systematic hardware issues. Systematic faults (see ISO 26262-1:2018, 3.165) are due to design or specification issues; software faults and a subset of hardware faults are systematic. At the component level, each different type of fault can lead to different failures. However, failures at the component level are faults at the item level. Note that in this example, at the vehicle level, faults from different causes can lead to the same failure. A subset of failures at the item level will be hazards (see ISO 26262-1:2018, 3.75) if additional environmental factors permit the failure to contribute to an accident scenario.

EXAMPLE If unexpected behaviour of the vehicle occurs while the vehicle is starting to cross an intersection, a crash can occur, e.g. the risk of the hazardous event “vehicle bucking when starting to cross intersection” is assessed for severity, exposure and controllability (_bucking_ refers to making sudden jerky movements).

Figure 5 — Example of faults leading to failures

NOTE 1 Possible implemented error detection and control on component or item level is not depicted in Figure 5.

NOTE 2 The failure of the component is the fault on the item level (indicated by the dot dot dashed arrow).

# 4.4 FTTI and emergency operation tolerant time interval

# 4.4.1 Introduction

ISO 26262-3:2018, 6.4.4.3 states in the NOTE that the FTTI can be included as part of a safety goal. Furthermore, ISO 26262-4:2018, 6.4.2.2 specifies that the FTTI and emergency operation tolerance time interval are to be taken into account in the definition of fault handling time interval for each safety mechanism.

NOTE Fault handling time interval is a characteristic for a given safety mechanism. Fault tolerant time interval (FTTI) is a characteristic of an item.

As a part of the process of determining safety goals and functional safety requirements at concept phase, the FTTI is specified on vehicle level based on vehicle functionality. This time span can be taken into consideration during product development, leading to the determination of the maximum fault handling time interval (i.e. sum of the fault detection time interval and the fault reaction time interval as described in ISO 26262-1:2018, Figure 5) needed to avoid a hazardous event. FTTI is a necessary value in order to design the response time of a safety mechanism. Within the FTTI, the fault is controlled by a safety mechanism and the occurrence of a hazardous event can be prevented. This is achieved when the sum of the fault detection time interval and the fault reaction time interval is shorter than the FTTI. An emergency operation (ISO 26262-4:2018, 6.4.2.2) is specified when a safe state cannot be reached within the FTTI. The emergency operation is an operating mode defined as part of the warning and degradation strategy. Emergency operation is initiated prior to the end of the FTTI and is maintained until the safe state is reached prior to the end of the emergency operation tolerance time interval.

To

meet the safety goal, a safe state has to be reached before the end of the emergency operation tolerance time interval.

# 4.4.2 Timing model — Example control system

# 4.4.2.1 Control system description

This sub-clause applies the concepts of fault detection time interval (FDTI), fault tolerant time interval (FTTI), fault reaction time interval (FRTI), emergency operation tolerance time interval (EOTTI) and diagnostic test time interval (DTTI) to a valve control system example. The system consists of a valve, position sensor, controller and an electrical motor. The function of the system is to control the valve to a desired position using the electric motor.

A hazardous event resulting from an unintended flow can occur if the valve is opened a percentage more than intended. As a fault reaction, the motor is de-energized by a separate circuit in combination with a mechanical spring which pulls the valve to a default fixed opening position. This fixed opening position limits the flow resulting in a safe state for the item.

# 4.4.2.2 Application of timing model to example control system

The specific failure mode considered in this example is a motor fault which drives the valve to its maximum opening position. This condition can be the result of motor shorted to power or other motor control issues. Four scenarios are considered.

- Scenario 1: System without any safety mechanism preventing the violation of the safety goal. A short in the motor occurs resulting in the valve reaching its maximum position. Because no safety mechanism is in place a hazardous event can occur once the FTTI is exceeded.
- Scenario 2: System with implemented safety mechanism without emergency operation and a safe state is achieved within FTTI. A short in the motor occurs resulting in the valve reaching its maximum position. The implemented safety mechanism de-energizes the valve motor and the mechanical spring returns the valve to a low flow position within the FTTI, preventing a hazardous event. The safety mechanism (the spring) is designed to operate indefinitely and the safe state can be infinite.
- Scenario 3: System with implemented safety mechanism which prevents a hazardous event within the FTTI, but emergency operation is needed to transit to a safe state. The safe state is achieved within the emergency operation tolerance time interval by restricting the vehicle operating state. A short in the motor occurs resulting in the valve reaching its maximum position. The implemented safety mechanism de-energizes the valve motor and the mechanical spring returns the valve to a low flow position within the FTTI. The safety mechanism (the spring) is only designed to operate for a limited amount of time, the EOTTI. Prior to the expiration of the EOTTI, the vehicle operating state is restricted such that the flow from the valve cannot cause a hazardous event.
- Scenario 4: System with implemented safety mechanism which prevents a hazardous event is within the FTTI but emergency operation is needed to transit to a safe state. However, the transition time takes longer than the EOTTI. As a consequence, the cumulated risk becomes unacceptable, exceeding the target specified in the functional safety concept. A short in the motor occurs resulting in the valve reaching its maximum position. The implemented safety mechanism de-energizes the valve motor and the mechanical spring returns the valve to a low flow position within the FTTI. The safety mechanism (the spring) is only designed to operate for a limited amount of time, the EOTTI. In this scenario, the vehicle operation is not restricted and the item is in emergency operation longer than the expiration of the EOTTI, resulting in an unreasonable risk of safety goal violation.

Figure 6 shows the timing model associated with the four scenarios. Figure 6 is based on ISO 26262-1:2018, Figure 4 and ISO 26262-1:2018, Figure 5.

Figure 6 — Timing model example based on ISO 26262-1:2018, Figure 4

Figure 6 includes 7 time stamps described below:

- t1 Time of diagnostic test prior to occurrence of the fault.
- t2 Occurrence of fault, fault not detected.
- t3 Detection of fault (e.g. due to error counter reaching its threshold, see ISO 26262-1:2018, 3.55 FDTI EXAMPLE), start of fault reaction time interval.
- t4 Transition to safe state completed (scenario 2), start of emergency operation (scenarios 3 and 4).
- t5 End of emergency operation (scenario 3).
- t6 Time limit for emergency operation.
- t7 Occurrence of hazardous event.

# 4.4.2.3 Warning and degradation strategy

When the valve is in the default position, it can have an impact at the vehicle level. The functional safety concept may also include a requirement to warn the driver when in this state. This is part of the warning and degradation strategy and is indicated by the “Driver warning telltale on” arrow on Figure 6 which can occur within a specified time after t3.

# 9 Safety Element out of Context

# 9.1 Safety Element out of Context development

The automotive industry develops generic elements for different applications and for different customers. These generic elements can be developed independently by different organizations. In such cases assumptions are made about the requirements and the design; including the safety requirements that are allocated to the element by higher design levels and on the design external to the element. Such elements can be developed by treating these as Safety Elements out of Context (SEooC). An SEooC is a safety-related element which is not developed for a specific item. This means, it is not developed in the context of a particular vehicle.

An SEooC can be a system, a combination of systems, a subsystem, a software component, a hardware component or a part. Examples of SEooC include system controllers, ECUs, microcontrollers, software implementing a communication protocol or an AUTOSAR software component. An SEooC cannot be an item as the development of an item always requires the context of a vehicle intended for series production. In the case where the SEooC is a system, this system is not developed in the context of a vehicle and therefore it is not an item.

SEooCs differ from qualified software components described in ISO 26262-8:2018, Clause 12 and evaluated hardware elements described in ISO 26262-8:2018, Clause 13:

- An SEooC is developed, based on assumptions, in accordance with the ISO 26262 series of standards. It is intended to be used in multiple different items when the validity of its assumptions can be established during integration of the SEooC.
- Qualification of software components and evaluation of hardware elements address the use of pre-existing software components or hardware elements for an item developed under the ISO 26262 series of standards. These are not necessarily designed for reusability nor developed under the ISO 26262 series of standards.

For software development, Table 4 describes the intended use of qualification, safety element out of context and the proven in use argument for different software components. For hardware development, an equivalent table could be constructed.

**Categorization of the software components**
|Categorization of Software Component|ISO 26262-6 in context of an item|ISO 26262-8:2018, Clause 12 Qualification of SW Component|ISO 26262-6 as Safety Element out of Context|ISO 26262-8:2018, Clause 14 Proven in use argument|
|---|---|---|---|---|
|Newly developed|Suitable|Not suitable|Suitable|Not suitable|
|Re-use with change|Suitable|Not suitable|Suitable|Suitablea|
|Re-use without change|Not suitable|Suitable|Suitable|Suitable (if originally developed as SEooC)|

a See ISO 26262-8:2018, 14.4.4.

When developing an SEooC, applicable safety activities are tailored as described in ISO 26262-2:2018, 6.4.5.7. Such tailoring for the SEooC development does not imply that any step of the safety lifecycle can be omitted. In case certain steps are deferred during the SEooC development they are completed during the item development.

The ASIL capability of an SEooC designates the capability of the SEooC to comply with assumed safety requirements assigned with a given ASIL. Consequently, it defines the requirements of the ISO 26262 series of standards that are applied for the development of this SEooC.

An SEooC is thus developed based on assumptions; on an intended functionality and use context which includes external interfaces. These assumptions are set up in a way that addresses a superset of items, so that the SEooC can be used later in multiple different, but similar, items. The validity of these assumptions is established in the context of the actual item while integrating the SEooC.

An item may contain multiple SEooCs, with SEooCs interfacing directly to each other. In this case the validity of the assumptions of one SEooC is established considering the interfacing SEooC. In a case where the validity of the assumptions made during the SEooC development cannot be established during its integration into the item, either a change to the SEooC or to the item can be made as described in ISO 26262-8:2018, Clause 8.

# 9.2 Use cases

# 9.2.1 General

The development of an SEooC involves making assumptions on the prerequisites of the corresponding phase in the product development, e.g. for a software component, which is a part of the software architectural design, the corresponding phase is ISO 26262-6:2018, Clause 7. It is not necessary to make assumptions on all prerequisites.

Figure 21 shows relationship between assumptions and SEooC development. The development of an SEooC can start at a certain hierarchical-level of requirements and design. Each individual requirement or design prerequisite is pre-determined in the status _assumed_. The correct implementation of the requirements for the SEooC (derived from the assumed high-level requirements and assumptions on the design external to the SEooC) will be verified during the SEooC development.

Figure 21 — Relationship between assumptions and SEooC development

The validation of these requirements and assumptions are then established during the development of the item. Similarly, verification activities demonstrate that a developed SEooC, at any level, is consistent with the requirements in the context where it is used. For example, when a software component, developed out of context, is used, the verification of the software specification can demonstrate that the requirements in the software architectural design specification are met. This verification report can be produced when development of the SEooC is finished and the item development reaches the phase where requirements on the safety element are formulated.

Some typical examples of SEooC are given below; namely a system, a hardware component and a software component.

# 9.2.2 Development of a system as a Safety Element out of Context example

This section is intended to show how the tailoring of the SEooC concept is applied to a new E/E system which can be integrated by different vehicle manufacturers.

For the purpose of this example, the system includes functionality to both activate a function under certain vehicle conditions and to allow the deactivation of the function on proper driver requests. The process flow is given in Figure 22.

NOTE 1 Some additional tailoring of the requirements can be necessary depending on the exact nature of the SEooC.

NOTE 2 Depending on the exact nature of the SEooC, some requirements of ISO 26262-3 and ISO 26262-4 cannot be applicable, and therefore only partial consideration is made.

NOTE 3 Although all the clauses of the ISO 26262 series of standards are not shown, this does not imply that they are not applicable.

Figure 22 — SEooC system development

Step 1a — Definition of the scope of SEooC

Based on assumptions, the SEooC developer defines the purpose, functionalities and external interfaces of the SEooC.

Examples of such assumptions on the scope of the SEooC can be:

- The system is designed for vehicles with a gross mass up to 1 800 kg.
- The system is designed for front-wheel driven vehicles.
- The system is designed for maximum road slope of 32 %.
- The system has interfaces with other external systems to get the required vehicle information.
- Functional requirements:
  - The system activates the function when requested by the driver under certain vehicle conditions;
  - The system deactivates the function when requested by the driver.

Step 1b — Assumptions on safety requirements for the SEooC

The development of an SEooC makes assumptions about the item definition, the safety goals of the item, and the corresponding functional safety requirements related to the SEooC functionality in order to identify the technical safety requirements of the SEooC.

Examples of assumptions on the functional safety requirements allocated to the SEooC can be:

- The system does not activate the function at high vehicle speeds (ASIL x).
- The system does not deactivate the functionality when the driver request is not detected (ASIL y).

To achieve the assumed safety goals, specific assumptions on the context are defined.

Examples of assumptions on the context of the SEooC can be:

- An external source will provide information at the requested ASIL enabling the system to detect the proper vehicle condition (ASIL x).
- An external source will provide information about the driver request at the requested ASIL (ASIL y).

Step 2 — Development of the SEooC

When the technical safety requirements have been derived from the assumed functional safety requirements of the item, the SEooC is developed following the requirements of the ISO 26262 series of standards.

Step 3 — Work products

At the end of the SEooC development, the work products that show that the derived technical safety requirements are fulfilled, are made available. All necessary information from the work products is then provided to the item integrator, including SEooC safety requirements and the assumptions made on the context.

Step 4 — Integration of the SEooC into the item

During item development, the safety goals and the functional safety requirements are specified. The functional safety requirements of the item are matched with the functional safety requirements assumed for the SEooC to establish their validity.

In the case of an SEooC assumption mismatch, a change management activity, beginning with an impact analysis, is conducted as described by ISO 26262-8:2018, Clause 8. Potential outcomes include:

- the difference can be deemed to be acceptable with regard to the achievement of the safety goal, and no action is taken.
- the difference can be deemed to impact the achievement of the safety goal and a change can be necessary to either the item definition or the functional safety concept.
- the difference can be deemed to impact the safety goal and a change is required to the SEooC component (including possibly a change of component).

# 9.2.3 Development of a hardware component as a Safety Element out of Context example

# 9.2.3.1 General

This section uses a microcontroller (MCU) as an example hardware component SEooC. The process flow is given in Figure 23.

NOTE 1 Some additional tailoring of the requirements can be necessary depending on the exact nature of the SEooC, e.g. to adapt target values for the probability to violate a safety goal due to random hardware failure.

NOTE 2 Depending on the exact nature of the SEooC, some requirements of ISO 26262-5 are not applicable, and therefore only partial consideration is made.

NOTE 3 Although all the clauses of the ISO 26262 series of standards are not shown, this does not imply that they are not applicable.

Figure 23 — SEooC hardware component development

# 9.2.3.2 Step 1 — Assumptions on system level

The development of an MCU (see Figure 23) as an SEooC starts (step 1) with an assumption of the system level attributes and requirements as per ISO 26262-2:2018, 6.4.5.7. This stage can be broken down into two sub-steps (1a and 1b) based on the analysis of some reference applications. The requirements are assumed with respect to the pre-requisites for HW product development (ISO 26262-5:2018, Table A.1); examples follow.

# 9.2.3.3 Step 1a — Assumptions on technical safety requirements

Below are some example assumed technical safety requirements created for an MCU.

# 9.2.3.3 Step 1a — Assumptions on technical safety requirements

a) Failures of the CPU instruction memory are mitigated by safety mechanism(s) in hardware with at least the target value (e.g. 90 %) assigned for the single-point fault metric at the HW part level (might also be expressed in terms of required DC).

b) The contribution of the MCU to the total probability of violation of a safety goal is no more than 10 % of the indicated probability for the relevant ASIL.

c) To achieve a safe state, the MCU drives all I/O outputs to a low state when reset is asserted.

d) Any safety mechanisms implemented related to the processing function completes in less than 10 milliseconds (assigned portion of the fault handling time interval on the appropriate level within the system architecture).

e) A memory protection unit is present to provide the possibility of separating software tasks with different ASILs.

ASIL capability is established at this step.

# 9.2.3.4 Step 1b — Assumptions on system level design

Some examples of system level design assumptions, external to the SEooC:

a) The system will implement a safety mechanism on the power supply to the MCU to detect over voltage and under voltage failure modes.

b) The system will implement a windowed watchdog safety mechanism external to the MCU to detect either clocking or program sequence failures of the MCU.

c) A software test will be implemented to detect latent faults in the EDC safety mechanism of the MCU.

d) A SW-based test is executed at key-on to verify the absence of latent faults in the logical monitoring of the program sequence of the CPU.

e) Debug interfaces of the MCU are not used during safety-related operation. Therefore, any faults in the debug logic will be considered safe faults.

# 9.2.3.5 Step 2 — Execution of hardware development

On the basis of these decisions (assumed technical safety requirements and assumptions related to the design external to the SEooC), the SEooC is developed (step 2) as written in ISO 26262-5 and each applicable work product is prepared. For example, the evaluation of safety goal violations due to random HW failures (see work product written in ISO 26262-5:2018, 9.5.1) is done considering the SEooC assumptions, including any budget for FIT rate found in the assumed technical safety requirements. On the basis of the SEooC assumptions, the safety analyses and the analysis of dependent failures internal to the MCU are performed referring to ISO 26262-9.

# 9.2.3.6 Step 3 — Work products

At the end of the MCU product development (step 3), the necessary information from the work products is provided to the system integrator. This includes the following documentation: assumed requirements, assumptions related to the design external to the SEooC and applicable work products of the ISO 26262 series of standards (for example, the report on the probability of a violation of a safety goal due to random HW failure).

# 9.2.3.7 Step 4 — Integration of the SEooC into the system

When the MCU developed as an SEooC is considered in the context of the item HW product development phase, the validity of all SEooC assumptions including SEooC assumed technical safety requirements.

and the assumptions related to the design external to the SEooC are established (step 4). It is plausible that mismatches between SEooC assumptions and system requirements will occur. For example, the item developer could decide not to implement an assumed external component. As a consequence, the evaluation of safety goal violations due to random HW failures done by the SEooC developer might no longer be consistent with the item.

In the case of an SEooC assumption mismatch, a change management activity beginning with impact analysis is conducted as written in ISO 26262-8:2018, Clause 8. Potential outcomes include:

- The difference can be deemed to be acceptable with regard to the achievement of the safety goal, and no action is taken.
- The difference can be deemed to impact the achievement of the safety goal and a change can be necessary to either functional safety concept or the technical safety requirements.
- The difference can be deemed to impact the achievement of the safety goal and a change is required to the SEooC component (including possibly a change of component).
- The difference can be deemed to impact the achievement of the safety goal, and therefore safety metrics are recalculated, but the recalculated metrics show that the design meets the system targets, so no change is necessary.

# 9.2.4 Development of a software component as a Safety Element out of Context example

# 9.2.4.1 General

This clause illustrates the different steps of the application of the SEooC concept to a new medium/low level software component. The process flow is given in Figure 24.

NOTE 1 Some additional tailoring of the requirements can be necessary depending on the exact nature of the SEooC.

NOTE 2 Depending on the exact nature of the SEooC, some requirements of ISO 26262-6 are not applicable, and therefore only partial consideration is made.

NOTE 3 Although all the clauses of the ISO 26262 series of standards are not shown, this does not imply that they are not applicable.

Figure 24 — SEooC software component development

# 9.2.4.2 Step 1a — Assumptions on the scope of the software component as an SEooC

This step is intended to state the relevant assumptions regarding the purpose of the software component, its boundaries, its target environment, its functionalities and its properties. Examples of such assumptions include:

- The software component is integrated into a given software layered architecture.
- Any potential interference caused by the software component is detected and handled by its environment.
- The software component provides the functions as specified in assumed software functional requirements.

# 9.2.4.3 Step 1b — Assumptions on the safety requirements of the software component

Step 1b is intended to make assumptions on higher level safety requirements that potentially impact the software component in order to derive its software safety requirements. For example, if a given set of data calculated by the software component is assumed to be of high integrity (ASIL x), then the resulting software safety requirements allocated to the SEooC can be:

- The software component detects any corruption on the input data which can violate safety goals (ASIL x);
- The software component signals the error conditions to be notified based on the assumed technical safety requirements (ASIL x);
- A default value is returned with a fault status for any error condition detected (ASIL x); and
- The software component returns the following results coded with CRC and a status (ASIL x).

# 9.2.4.4 Step 2 — Development of the software component

Once the necessary assumptions on the software component are explicitly stated, the SEooC is developed
in accordance with the requirements of ISO 26262-6 corresponding to its ASIL capability (ASIL x in this
example). All applicable work products are made available for further integration in different contexts,
including the work products related to the verification of the assumed software safety requirements.

# 9.2.4.5 Step 3 — Integration of the software component in a new particular context

Before the software component is integrated with other software components in a new particular
context, the validity of all the assumptions made on this SEooC are checked with regard to this
context. This includes the assumed software safety requirements with their ASIL capability and all the
assumptions made on the purpose, boundaries, target environment, functionalities and properties of
the software component (see 9.2.4.2 and 9.2.4.3).

In the case where some assumptions regarding the software component do not fit with this new context,
an impact analysis is initiated in accordance with ISO 26262-8:2018, Clause 8. Potential outcomes of the
impact analysis include:

- The discrepancies are acceptable with regard to the achievement of the safety requirements
  applicable at the software architectural design level, and no further action is taken.
- The discrepancies impact the achievement of the safety requirements applicable at the software
  architectural design level and a change can be necessary to these requirements in accordance with
  ISO 26262-8:2018, Clause 8.
- The discrepancies impact the achievement of the safety requirements applicable at the software
  architectural design level and a change is required to the SEooC component (including possibly a
  change of component) in accordance with ISO 26262-8:2018, Clause 8.

NOTE In the case where the integration of a software component in a particular software architectural
design results in the coexistence of software safety-related elements that have different ASILs assigned, the
criteria for coexistence of elements are fulfilled as described in ISO 26262-9:2018, Clause 6, or alternatively the
elements with lower ASILs are upgraded to the higher ASIL.

# 10 An example of proven in use argument

# 10.1 General

The item and its requirements described in this clause are an example. The safety goal, its ASIL and the
following requirements are given to illustrate the proven in use argument defined in ISO 26262-8:2018,
Clause 14 (proven in use argument). This example does not reflect what the application of the ISO 26262
series of standards on a similar real-life example would be.

# 10.2 Item definition and definition of the proven in use candidate

A vehicle manufacturer wants to integrate new functionality into a new vehicle. For the purpose of this example, the item implementing this functionality is composed of sensors, one ECU that includes the complete hardware and software necessary to implement the functionality, and one actuator. The incorrect activation of the functionality is ranked ASIL C by the vehicle manufacturer. The corresponding safety goal is derived into an ASIL C functional safety requirement allocated to the ECU. The supplier of the ECU proposes to carry over an existing ECU already in the field. The differences between the previous use of the ECU and its intended use in the new application are analysed. The analysis shows that the software will be modified to implement the new functionality by changing calibration data, but the ECU hardware can be carried over without modification. The supplier intends to substitute the demonstration of compliance to requirements of ISO 26262-5 by a proven in use argument for the hardware of the ECU. The hardware of the ECU is therefore the proven in use candidate.

# 10.3 Change analysis

To establish a proven in use credit, the supplier performs a change analysis of the proven in use candidate. This analysis shows that no change that could have an impact on the safety behaviour of the proven in use candidate has been introduced since the beginning of its production. Moreover, the analysis shows that the differences between the previous use of the proven in use candidate and its intended use have no safety impact:

- the candidate’s boundary is within the specification limits;
- the previous integration environment requires the same technical behaviour; and
- the cause and effects at the boundary of the candidate are the same in the previous and future integration environments.

# 10.4 Target values for proven in use

To establish the validity of the proven in use argument, the supplier estimates the number of cumulated hours the proven in use candidate has been in the field. The supplier also analyses the field data from the service period for any safety-related event, i.e. any reported event that would potentially cause, or contribute to, the violation of a safety goal or a safety requirement regarding the intended usage of the candidate in the new item. The estimation of the duration of the service history is performed, based on the number of produced vehicles embedding the proven in use candidate, together with their production date, and data on the typical usage of a vehicle in this segment of the market (number of driving hours per year). The service history is based on the field return of the different vehicles embedding the proven in use candidate:

- Warranty claims;
- In-the-field defects analyses; or
- Return of defective parts from the vehicle manufacturers.

At the date of the initiation of the hardware development of the item, these analyses show that no safety-related event has occurred in the field. The total cumulated driving hours are estimated to be less than the target for the definite proven in use status for an ASIL C, but meets the interim service period as defined in ISO 26262-8:2018, 14.4.5.2.5.

The conclusion is then as follows:

- The development of the item can carry on taking credit that the hardware of the ECU is provisionally anticipated to be proven in use.
- The field observation continues to obtain a definite proven in use status (see ISO 26262-8:2018, 14.4.5.2.5 and ISO 26262-8:2018, 14.4.5.2.6)

# 11 Concerning ASIL decomposition

# 11.1 Objective of ASIL decomposition

The objective of ASIL decomposition is to comply with the safety goal by using multiple sufficiently independent elements with respect to systematic faults.

# 11.2 Description of ASIL decomposition

ASIL decomposition refers to the allocation of redundant safety requirements to sufficiently independent elements of the item. Redundancy in this context does not necessarily imply classical modular redundancy (see ISO 26262-1:2018, 3.122).

EXAMPLE The main processor of an ECU can be monitored by a redundant monitoring processor, both of which are independently capable of initiating a defined safe state, even if the monitoring processor is not able to fulfil the functional requirements allocated to the ECU.

ASIL decomposition can only be understood in the context of systematic failures, that is, the methods and measures applied to reduce the likelihood of these failures. The requirements on the evaluation of the hardware architectural metrics and the evaluation of safety goal violations due to random hardware failures will remain unchanged by ASIL decomposition (See ISO 26262-9:2018, 5.4.5).

EXAMPLE In the case of an ASIL B(D) decomposition, the ASIL D target for the evaluation of the hardware architectural metrics is not decomposed into separate ASIL B targets for each HW element. As written in ISO 26262-5:2018, 8.2, target values can be assigned to hardware elements, but those targets are assigned case-by-case based on an analysis started at the level of the whole hardware of the item. The target metric according to the safety goal applies at the item level.

In such a decomposed architecture, the safety requirement before decomposition is only violated if both elements simultaneously violate their safety requirements resulting from the decomposition.

The possible decompositions in the ISO 26262 series of standards are described in ISO 26262-9:2018, Clause 5.

# 11.3 An example of ASIL decomposition

# 11.3.1 General

The item and its requirements described in this clause are examples. The safety goal, its ASIL, and the following requirements are only designed to illustrate the ASIL decomposition process. This example does not reflect what the application of the ISO 26262 series of standards on a similar real-life example would be.

# 11.3.2 Item definition

Consider the example of a system with an actuator that is triggered on demand by the driver using a dashboard switch (see Figure 25). For the purpose of this example, the actuator provides a comfort function if the vehicle is at zero speed, but can cause hazards if activated above 15 km/h.

For the purpose of this example, the initial architecture of the item is as follows:

- The dashboard switch input is read by a dedicated ECU (referred to as _Actuator Control ECU (AC ECU)_ in this example), which powers the actuator through a dedicated power line.
- The vehicle equipped with the item is also fitted with an ECU which is able to provide the vehicle speed. For the purpose of this example, the ability of this ECU to provide the information that the vehicle speed is greater than 15 km/h is assumed to be compliant with ASIL C requirements. This ECU is referred to as _VS ECU_ in this section.

Figure 25 — Item boundary

# 11.3.3 Hazard analysis and risk assessment

The hazardous event considered in the analysis is the activation of the actuator while driving at a speed above 15 km/h, with or without a driver request. For the purpose of the example, the ASIL associated to this hazardous event is classified as ASIL C.

# 11.3.4 Associated safety goal

Safety Goal 1: Avoid activating the actuator while the vehicle speed is greater than 15 km/h: ASIL C

# 11.3.5 System architectural design

The following lists the purpose of the initial architectural elements:

- The VS ECU provides the Actuator Control ECU (AC ECU) with the vehicle speed.
- The AC ECU monitors the driver\'s requests, tests if the vehicle speed is less than or equal to 15 km/h, and if so commands the actuator.
- The actuator is activated when it is powered.

# 11.3.6 Functional safety concept

# 11.3.6.1 General

This example of a Functional Safety Concept is only being used as an illustration of the ASIL decomposition. It is not intended to be exhaustive and does not include all the functional safety requirements.

- Requirement A 1: The VS ECU sends the accurate vehicle speed information to the AC ECU. → ASIL C
- Requirement A 2: The AC ECU does not power the actuator if the vehicle speed is greater than 15 km/h. → ASIL C
- Requirement A 3: The actuator is activated only when powered by the AC ECU. → ASIL C

# 11.3.6.2 Evolved safety concept of the item

The developers can choose to introduce a redundant element, here a Redundant Switch, as illustrated in Figure 26. By introducing this redundant element, the AC ECU is developed with an ASIL that is equal to or lower than ASIL C, in accordance with the results of an ASIL decomposition.

Figure 26 — Second iteration on the item design

Purpose of these elements (evolved architecture):

- The VS ECU control unit provides the AC ECU with the vehicle speed.
- The AC ECU monitors the driver's requests, tests if the vehicle speed is less than or equal to 15 km/h, and if so commands the actuator.
- The Redundant Switch is located on the power line between the AC ECU and the actuator. It switches on if the speed is less than or equal to 15 km/h, and off whenever the speed is greater than 15 km/h. It does this regardless of the state of the power line (its power supply is independent).
- The actuator operates only when it is powered.

Functional safety requirements:

- Requirement B 1: the VS ECU sends accurate vehicle speed information to the AC ECU. → ASIL C
- Alternatively: the incorrect transmission that vehicle speed is less than or equal to 15 km/h is prevented. → ASIL C
- Requirement B 2: the AC ECU does not power the actuator if the vehicle speed is greater than 15 km/h. → ASIL X(C) (see Table 5)
- Requirement B 3: the VS ECU sends accurate vehicle speed information to the Redundant Switch. → ASIL C
- Requirement B 4: The Redundant Switch is in an open state if the vehicle speed is greater than 15 km/h. → ASIL Y(C) (see Table 5)
- Requirement B 5: The actuator operates only when powered by the AC ECU and the Redundant Switch is closed. → ASIL C

To permit an ASIL decomposition, the developers add an independency requirement if deemed necessary:

- Requirement B 6: Sufficient independence of the AC ECU and the Redundant Switch is shown. → ASIL C

The original requirement A 2 has been replaced by the redundant requirements B 2 and B 4, both of which comply with the safety goal, and therefore ASIL decomposition can be applied.

|               | Requirement B 2: ASIL X(C) | Requirement B 4: ASIL Y(C) |
| ------------- | -------------------------- | -------------------------- |
| Possibility 1 | ASIL C(C) requirements     | QM(C) requirements         |
| Possibility 2 | ASIL B(C) requirements     | ASIL A(C) requirements     |
| Possibility 3 | ASIL A(C) requirements     | ASIL B(C) requirements     |
| Possibility 4 | QM(C) requirements         | ASIL C(C) requirements     |

# 12 Guidance for system development with safety-related availability requirements

# 12.1 Introduction

For many E/E systems, the loss of functionality cannot lead to a hazard. Therefore, the safe state can be achieved by switching off the functionality in case of a malfunction within the system. However, in some cases the HARA can show that the loss of a certain functionality can lead to a hazardous event. This can lead to a safety goal specifying a safety-related availability requirement.

The term _fault tolerance_ is used in a restricted sense within this clause. Within this clause the term _fault tolerance_ is only used in the context where the specified functionality is the intended functionality or a subset of the intended functionality that is to be provided in the presence of one or more faults (see ISO 26262-1:2018, 3.60). This clause does not address the context where the specified functionality is used to switch off the system. This clause does not address the context where a safe-state can be directly reached by switching off the functionality.

NOTE 1 There are various measures to ensure sufficient availability, including fault tolerance, fault avoidance and fault forecasting, where fault tolerance means the capability to deliver a specified functionality for at least a limited time after a fault belonging to a specified fault set has occurred. Fault avoidance means measures to reduce the occurrence of a fault and fault forecasting means the capability to detect a fault or degradation before it can lead to a failure.

NOTE 2 In case of fault tolerance not every imaginable fault can be tolerated. For clarification, the tolerable fault sets (e.g. single bit faults in case of an ECC with single error correction, double error detection capability) are specified.

# 12.2 Notes on concept phase when specifying fault tolerance

# 12.2.1 General

The following topics are considered in the concept phase when specifying fault tolerance:

- a) vehicle operating states in which the availability of a functionality is safety-related;
- b) faults to be tolerated;
- c) prevention of a hazardous event after a fault has occurred;
- d) operation after the item fault reaction;
- e) safe state to be achieved after a fault has occurred;
- f) ASIL decomposition of fault tolerant items; and
- g) safety requirements on other items.

# 12.2.2 Vehicle operating states in which the availability of a functionality is safety-related

Whether the loss of the availability of an item’s functionality can lead to a hazardous event or not depends on the vehicle operating state. For example, the loss of the functionality can lead to a hazardous event in a specific vehicle operating state (e.g. steering at high vehicle speeds) whereas in another vehicle operating state (e.g. steering at zero vehicle speed) it might not. If the vehicle is in a vehicle operating state in which the loss of the functionality does not lead to a hazardous event, then the availability of the functionality is considered not safety-related.

The measures to fulfil the safety related availability requirement are based on possible interactions with other item(s), the system architecture including other technologies (e.g. mechanical backup) and the results of safety analyses. If fault tolerant measures are adopted, 12.2.3 and 12.2.4 are applicable.

NOTE If the vehicle operating state is maintained by other items, possible new or changed hazards for these items are considered and the HARA is re-evaluated, if necessary.

EXAMPLE System X is an E/E system without mechanical back up. When driving at high speeds on country roads, the sudden loss of its functionality is difficult to control and can lead to a hazardous event with an ASIL rating. At very low speeds, the sudden loss of its functionality can be controlled easily by applying a different function from an available and sufficiently independent system Y, resulting in a C0 classification. So, in the vehicle operating state “item in normal operating mode at high vehicle speeds” the availability of its functionality is considered to be safety-related while in the vehicle operating state “item in normal operating mode at very low vehicle speeds” the availability of the functionality is not considered to be safety-related.

# 12.2.3 Prevention of hazardous events after a fault

# 12.2.3.1 Allowable time-span from the occurrence of a fault to completion of fault reaction

As part of the safety requirements, the maximum fault handling time interval consistent with the fault tolerant time interval of the item is specified.

# 12.2.3.2 Functions and performance to be maintained after fault reaction

For the case that the fault can cause the loss of the intended functionality or a subset of the intended functionality, and this loss can result in a hazardous event, the functions and the performance to be maintained after the occurrence of the fault are specified in order to transition to a safe state, transition between safe states or maintain a safe state.

NOTE Such functions and performance are provided during emergency operation or in the safe state.

EXAMPLE A hazardous event can only occur if the item output performance drops below 50% of its specified maximum output. The item is composed of two systems each of which is capable of providing 50% of the maximum specified output. If one system fails, the hazardous event can be prevented by switching off the faulty system while the other one maintains up to 50% of the maximum specified output.

# 12.2.4 Operation after fault reaction

# 12.2.4.1 Emergency operation

During emergency operation, the item is still free from unreasonable risk even though the ASIL capability of the item is lower than the ASIL rating of the possible hazard. To address this situation, the operating time in this state is limited, such that it is unlikely that an additional fault occurs which leads to a violation of the safety goal.

NOTE 1 The emergency operation tolerance time interval is defined and verified from the probability of a next fault in accordance with 12.3.1.

NOTE 2 The transition to the emergency operation is defined and verified to be safe.

# 12.2.4.2 Safe states for fault tolerant item

In the context of fault tolerant behaviour, typically one of the following two safe states is chosen:

a) A vehicle operating state in which the specified functionality is no longer needed for safety reasons. In this case, the specified functionality is permanently switched-off and thus no longer provided until the item is repaired; or

b) The possible vehicle operating states are limited in such a way that the ASIL rating of the hazardous events which can occur in the limited vehicle operating states is equal to or lower than the ASIL capability of the remaining system. In this case the specified functionality of the limited operating states provided by the remaining system can be interpreted as an item in its own right and can be operated without time restrictions. The possible vehicle operating states will return to unlimited once the item is repaired.

NOTE 1 The restrictions of the possible vehicle operating states can have an impact on the E, C and S parameters of the possible hazardous event.

EXAMPLE 1 Limiting the vehicle speed can reduce the severity and can improve the controllability of the hazardous event resulting in a lower ASIL rating than without the limitation.

NOTE 2 The exposure E in this HARA evaluation does not consider the occurrence of the fault.

NOTE 3 This ASIL rating can be used to:

- Restrict ASIL decompositions for items (12.2.6).
- Specify safety requirements for individual redundant components constituting the item. This includes determination of the ASIL capability of the remaining system in case of the loss of one redundant component.

NOTE 4 If a safety goal for an item is to maintain full or degraded functionality in the presence of a fault then the HARA can be extended to cover the functionality of the restricted vehicle operating states.

NOTE 5 If after the occurrence of the fault, the vehicle operating states are not changed (e.g. the vehicle operation is unrestricted without warning), then the ASIL is the same as that derived from the vehicle operating states without fault (the original HARA is applicable).

NOTE 6 The safety mechanism implementing the restrictions of the possible vehicle operating states inherits the original ASIL of the safety goal. If the safe state is reached or maintained with the support of functions of other items, these are identified as safety requirements on those items.

EXAMPLE 2
The ASIL of the safety goal of the item, in absence of faults, is _D_, Controllability = C3, Severity = S3 and the Exposure = E4 and if in the operating state of the degraded functionality, the controllability is improved, for example, to C2 then the ASIL requirements within this operating state is ASIL C: S3, E4, C2.

EXAMPLE 3
A by-wire system in the presence of a fault restricts vehicle operation to a low speed where most drivers can prevent a collision via another system. This could improve Controllability and can also reduce Severity in the vehicle speed restricted state.

NOTE 7
Once a safe state is reached, and the operator is notified, any repairs are the responsibility of the vehicle owner/operator as per the Vienna Convention on Road Traffic [17].

# 12.2.4.3 Emergency operation time interval

For a fault tolerant item, once a fault occurs the specified functionality is maintained and the item transitions to a safe state in accordance with 12.2.3.2. During the transition to a safe state, the fault reaction at vehicle level occurs (e.g. limiting vehicle speed to 30 km/h). However, before completing vehicle level fault reaction, a possible hazardous event caused by another fault occurring during the emergency operation time interval is not mitigated.

To minimize the risk, the emergency operation time interval is limited to the emergency operation tolerance time interval defined as a part of the safety concept.

NOTE 1
For determining the emergency operation tolerance time interval, the following are considered:

- physical system limitations;
- additional safety requirements for the hardware and software elements used during emergency operation, if required; and
- possibility of remaining system failing in a common way.

NOTE 2
Regarding random hardware faults, ISO 26262-5:2018, 9.4.2.4 e) can ensure the effectiveness of the hardware architecture in mitigating random hardware faults by taking the emergency operation time interval into account as an exposure duration.

NOTE 3
Ensuring that the emergency operation time interval does not exceed the emergency operation tolerance time interval is not always the responsibility of the vehicle manufacturer. This can also be the responsibility of the driver of the vehicle.

EXAMPLE
One of the headlight bulbs is burned out. The failure is detected and the driver is informed about the failure. It is the responsibility of the driver to repair the headlights within a reasonable amount of time.

# 12.2.5 Fault tolerant item example

# 12.2.5.1 Introduction

An example is used to describe possible flow of events related to behaviours of fault tolerant systems. This will illustrate the application of the various fault time interval notations.

# 12.2.5.2 Assumptions

The HARA for the item shows that a significant loss of the specified functionality for longer than a time x can lead to a hazardous event with an ASIL rating which is dependent on vehicle speed (vvehicle) at the time when the loss of the specified functionality occurs. In this example, it is assumed, with respect to HARA, that the exposure of the operational situation does not change for vvehicle. Therefore, the safety goal is formulated under the assumption of worst case conditions.

The safety goal in this example is formulated as:

- — avoid significant loss of the specified functionality for longer than a time x (the FTTI) (ASIL D).

NOTE Significant loss of the specified functionality means the output performance of the function is below the minimally required performance level.

# 12.2.5.3 Strategies of the example

Two strategies are considered to realize the safety goal assumed in 12.2.5.2.

- — Strategy 1: The item maintains the specified functionality after occurrence of a fault. The functionality is kept operating until the item is repaired. The vehicle operating state is not restricted until repair. In this case, the item is repaired within an allowable time interval (i.e. the emergency operation tolerance time interval).
- — Strategy 2: The item maintains the specified functionality after occurrence of a fault. The functionality is kept to the limited vehicle operating state without time limitation. In this case, the vehicle reaches the limited vehicle operating state within the allowable time interval (i.e. the emergency operation tolerance time interval).

# 12.2.5.4 System architecture description of the item

The item description for the example is provided below:

- — The item consists of two sufficiently independent channels, channel A and channel B.
- — Channel A provides the nominal function.
- — Channel B is a backup system. Its performance is greater than minimally required performance level which is the functionality necessary for a safe operation. The sufficiency of this functionality is validated according to ISO 26262-4:2018, Clause 8.
- — If channel A fails leading to a significant loss of functioning capability, channel B is activated within time x to prevent the violation of the safety goal.
- — Each one of channel A and channel B can, by itself fulfil the safety requirements on an ASIL D level as far as systematic faults are concerned.
- — The combination of channel A and channel B can fulfil the safety requirements on an ASIL D level as far as random hardware faults (e.g. ≤ 1 % of the random hardware faults can lead to a significant loss of the functionality) are concerned.

NOTE Other safety goals can exist leading to additional safety requirements for the elements of the item. These are not considered within this discussion.

This example considers two strategies which differ on the capability of channel B:

Strategy 1: Repair within emergency operation tolerance time interval

- — Channel B by itself does not fulfil the safety requirements for random hardware faults on an ASIL D level.
- — When the loss of channel A is detected, the driver is notified and the driver is required to repair the item within the emergency operation tolerance time interval. The probability of fault occurrence during emergency operation time interval is taken into account as part of the PMHF calculation and can also be ensured by methods in 12.3.

Strategy 2: Limited operation without time restrictions

- — Channel B by itself does not fulfil the safety requirements for random hardware faults on an ASIL D level. It can only fulfil the safety requirements as far as random hardware faults are concerned on an ASIL A level, i.e. it only has an ASIL A capability regarding this safety goal. It achieves this via fault prevention measures only.

- The HARA for the item in which ASIL rating depending on vehicle is referred. In this example, ASILs are assumed as:
  - if the maximum vehicle speed is not limited, the rating is ASIL D;
  - if the maximum vehicle speed is limited to v4, the rating is ASIL C;
  - if the maximum vehicle speed is limited to v3, the rating is ASIL B;
  - if the maximum vehicle speed is limited to v2, the rating is ASIL A;
  - if the maximum vehicle speed is limited to v1, the rating is QM;
  - if the maximum vehicle speed is limited to v0, no hazard can occur.

NOTE This safety goal is rated ASIL D as the possible vehicle operating states are not limited (i.e. vvehicle > v4). However, for specific driving situations (e.g. vvehicle < v2), either certain hazards cannot occur or the S, C and E ratings are not the same as worst case assumption. This results in an overall lower ASIL requirement for this hazard. In this example, the hazard is only rated ASIL D for higher vehicle speeds. If the vehicle speed is equal or less than v2, then better controllability and less severity than for higher vehicle speeds are assumed and the resulting hazard from significant loss of the specified functionality is rated as an ASIL A.

- The vehicle speed is reduced to less than v2 by other items and this function is an additional safety requirement for such item with ASIL D. This is a prerequisite for implementing Channel B in strategy 2.

# 12.2.5.5 Flow of events for this example

Figures 27 and 28 show examples which describe the concepts of FTTI, fault detection and fault reaction time, emergency operation and safe state in the context of a safety-related availability requirement addressed by a fault tolerant system with strategy 1 and strategy 2 respectively. In these figures, the same time scales are used to clarify the difference between the two strategies.

Figure 27 — Example vehicle speed history for strategy 1

Figure 28 — Example vehicle speed history for strategy 2

Figure 27 and 28 events t1 through t6 are:

- t1: time when a fault manifests itself as a significant loss of the specified functionality;
  A fault in channel A manifests itself as a loss of channel A, which results in a significant loss of the
  specified functionality. The loss of the function occurs at vvehicle > v4 which could result in an ASIL
  D rated hazard.
- t2: time when the fault is detected;
  The significant loss of the specified functionality is detected by a safety mechanism. This occurs in
  both strategies.

NOTE: The time span between t1 and t2 is also referred to as the fault detection time interval.

- t3: time when the item completes changing its operation mode, end of the fault reaction time interval;
  As an error reaction, channel B is activated providing the required functionality. As the required
  functionality is provided within a time less than x, i.e. t1 < t3 < t1 + x, the hazard is prevented.
  In strategy 1, the occurrence of the fault is notified to the driver by means specified as part of the
  warning and degradation strategy.
  In strategy 2, deceleration within v2 starts at this time.

NOTE: The safety requirement to reduce the vehicle speed to v2 has an ASIL D rating. Therefore, the
function to reduce and maintain the vehicle speed to v2 needs an ASIL D capability.

- t4: end of fault tolerant time interval;
  t4 = t1 + x. The time x corresponds to the FTTI. If the significant loss of specified functionality lasts
  for t4 or longer, an ASIL D rated hazardous event can occur. This occurs in both strategies.
- t5: time when the item reaches the safe state, t5–t3 is defined as the emergency operation
  time interval;
  In strategy 1, the item is repaired at this point. Before the item is repaired, vehicle operating state
  is not limited. Depending on the warning and degradation strategy, t5 is reached at the end of one
  trip or after several drive cycles.
  In strategy 2, the vehicle speed reached vvehicle < v2, at this point of time. In this state, a significant
  loss of the specified functionality (e.g. due to failure of channel B) can only lead to an ASIL A rated
  hazard. Since the remaining effective safety measures support the safety goal up to an ASIL A, i.e.
  channel B has an ASIL A capability regarding this safety goal, the operating state of the item can be
  considered to be without an unreasonable level of risk.

NOTE: The time between t3 and t5, the emergency operation time interval, can also be considered as
free from unreasonable risk not due to the achieved amount of risk reduction but due to the argument that
the item spends a limited time in this vehicle operating state.

- t6: maximum allowable time to reach the safe state, t6–t3 is defined as the emergency operation
  tolerance time interval;
  The allowable time span from t3 to reaching the safe state is defined as the emergency operation
  tolerance time interval. The emergency operation tolerance time interval is t3 + y and is the latest
  point in time.
  In strategy 1, t6 is the expected time until when the item is repaired.
  In strategy 2, t6 is the target time when the limitation of the vehicle speed to vvehicle < v2
  can be achieved.

NOTE: For items where availability is not safety-related, the item reaches the safe state within t4.

# 12.2.6 ASIL decomposition of fault tolerant items

The basic idea of ASIL decomposition is that an initial safety requirement with ASIL X is decomposed
into a combination of redundant safety requirements with ASIL Y1(X) and ASIL Y2(X). The target risk
reduction is achieved by the combination of decomposed redundant safety requirements and is not
achieved by one of them alone. This approach is also applicable to fault tolerant items with redundancy
implementing decomposed safety requirements. Therefore, there are no additional restrictions on
ISO 26262-9:2018, Clause 5.

NOTE Fault tolerant items need to demonstrate sufficient independency (see ISO 26262-9:2018, 5.4.3)
If the ASIL decomposition is applied to the redundant elements of a fault tolerant item, then the design
decisions consider both the result of ASIL decomposition and the result of the hazard analysis and risk
assessment of the item applied to the state after the loss of redundancy [in case of 12.2.4.2 b)].

The ASILs of redundant safety requirements are assigned considering:

- the required minimum ASIL for maintaining operation of the item after the loss of redundancy; and
- the ASIL resulting from the decomposition of an initial safety requirement.

EXAMPLE An item has an ASIL D safety goal that “The loss of more than 60 % of the output capability for
longer than X shall be prevented”. The item is implemented as two independent components, each providing
50 % of the desired output. The two outputs are summed together (Figure 29). Each component has sufficient
authority to maintain the intended service above 40 % and is sufficient to maintain control and prevent a hazard.
In response to the failure of one of the components, the vehicle operates in a degraded mode because its
performance is limited independently of the remaining component. A hazard analysis and risk assessment
determines an ASIL B level for operation during degraded mode because the vehicle performance is limited by
another item and the malfunction during degraded mode is mitigated from initial operating mode with ASIL D to
satisfy the original safety goal.

Figure 29 — Fault Tolerant Item consisting of two independent components summed together

ISO 26262-9:2018 5.4.9, allows the following ASIL decomposition pairs for the two requirements
implemented into independent components:

- a) ASIL C(D) and ASIL A(D);
- b) ASIL B(D) and ASIL B(D); and
- c) ASIL D(D) and QM(D).

However, for a design decision that restricts the ASIL of the item's safety goals to ASIL B, when the
vehicle performance is limited, the minimum ASIL capability for each component would be ASIL B and
the most suitable decomposition for this design decision is b) ASIL B(D) and ASIL B(D). Options a) and
c) are not suitable unless the ASIL of the remaining component is raised to at least ASIL B [i.e. ASIL C(D)
and ASIL B(D) or ASIL D(D) and ASIL B(D)].

# 12.3 Availability considerations during hardware design phase

# 12.3.1 Random hardware fault quantitative analysis

# 12.3.1.1 Emergency Operation Tolerance Time Interval calculation method

For systems where fault tolerance is achieved using redundancy, once the system has completed the fault reaction to the first fault, the system is in an operating mode without redundancy. If the ASIL capability of the system with such an operating mode does not meet the ASIL derived from the vehicle operating state, the amount of time allowable to stay in this vehicle operating state is limited to reduce the risk of a second fault. This is a possible factor to determine emergency operation tolerance time interval and the rationale of the time is confirmed by quantitative analysis required by ISO 26262-5:2018, Clause 9. If the method of ISO 26262-5:2018, 9.4.2 is used to determine the metric for random hardware failure, the PMHF estimation considering the Emergency Operation Tolerance Time Interval (Teotti) satisfies the PMHF target. Alternatively, the PMHF can be used to calculate a limit for Teotti with respect to the risk of safety goal violation from a subsequent random hardware fault of an element.

NOTE Since the PMHF value itself has no absolute significance (see ISO 26262-5:2018, 9.4.2.2, NOTE 1), using it to calculate Teotti is one option. Other quantitative or qualitative approaches are possible.

The Teotti can also be restricted by considering it as a property of the item state after the occurrence of the fault or loss of redundancy. For this state, appropriateness of the Teotti is decided by comparing the probability metric of violating the safety goal over the expected usage of the vehicle (PMHF × Tlifetime) to the probability metric of violating the safety goal while operating without redundancy. A sample formula (making a first order approximation) is given in Equation (1):

Teotti ≤ Tlifetime × λtarget / λdegr (1)

where

- λtarget is the target PMHF (derived in accordance with ISO 26262-5:2018, 9.4.2.2) corresponding to the ASIL rating of the item after the occurrence of the fault or loss of redundancy. Without any specification for the degraded mode or emergency operation, the initial ASIL is used;
- λdegr for the item state after the occurrence of the fault or loss of redundancy, the average probability per hour over the Emergency Operation Tolerance Time Interval of a failure that results in a violation of the safety goal.

The specific formula depends on the system architecture and detailed design.

# 12.3.1.2 Example — Dynamic redundant architecture with standby

Figure 30 shows a dynamic redundant architecture with standby which is used to demonstrate the calculation of Teotti.

Figure 30 — Example — Dynamic redundant architecture with standby

This case is analogous to the example of 8.3.2.2 with Module 1 as the IF and Module 2 as the SM1. The formula for the PMHF is the same as the one given in 8.3.2.4 with Tservice replaced with Teotti. For this system, Teotti can now be calculated as Equation (2):

Teotti ≤ (MPMHF – λSPF – λRF – 0,5 × λSM1,DPF,latent × λIF,DPF × Tlifetime – 0,5 × λIF,DPF,latent × λSM1,DPF × Tlifetime) / (λSM1,DPF,detected × λIF,DPF + λIF,DPF,detected × λSM1,DPF) (2)

Equation (1) can also be determined using λtarget = MPMHF and λdegr = λSM1,DPF as:

Teotti ≤ Tlifetime × MPMHF / λSM1,DPF (3)

Table 6 compares the results from the two equations for Tlifetime = 10 000 h and two sets of failure rates. For Case 1, Equation (3) is the limiting factor and Teotti ≤ 167 h. For Case 2, Equation (2) is the limiting factor and Teotti ≤ 31 h.

The emergency operation tolerance time interval is specified as a part of the functional safety requirements. In this example, the appropriateness of the EOTTI is confirmed by considering both methods described in 12.3.1.1, illustrated by Equations (2) and (3). Equation (2) gives the amount of margin for the emergency operation tolerance time interval for a given PMHF target and element failure rates and latent diagnostic test time intervals. On the other hand, Equation (3) calculates an additional limitation for Teotti as a property of the item state after the occurrence of the fault or loss of redundancy.

Table 6 — Example values, Equations (2) and (3)

| Lambdas (h−1) | Case 1 | Case 2 |
| ------------- | ------ | ------ |
| PMHF          | 1,0E-7 | 1,0E-7 |
| SF            | 2,0E-9 | 2,0E-9 |
| RF            | 1,2E-8 | 6,0E-8 |

Table 6 (continued)

| Lambdas (h−1)    | Case 1 | Case 2 |
| ---------------- | ------ | ------ |
| IF,DPF           | 6,0E-6 | 6,0E-6 |
| IF,DPF,DETECTED  | 5,4E-6 | 5,4E-6 |
| IF,DPF,LATENT    | 6,0E-7 | 6,0E-7 |
| SM1,DPF          | 6,0E-6 | 6,0E-6 |
| SM1,DPF,DETECTED | 5,4E-6 | 5,4E-6 |
| SM1,DPF,LATENT   | 6,0E-7 | 6,0E-7 |

Results

| Equation | Value |
| -------- | ----- |
| (2)      | 772 h |
| (3)      | 167 h |

NOTE 1: ISO 26262-5:2018, 9.4.2.4 gives the mean duration of a vehicle trip can be considered as being equal to 1 h.

EXAMPLE: To allow operation of a system for 10 trips or key cycles after the occurrence of the fault, the Emergency Operation Tolerance Time Interval needs to be greater or equal to 10 h.

NOTE 2: If the resulting Teotti based on the PMHF calculation is too restricted, then other parameters such as residual failure rates can be addressed to relax the restriction of Teotti.

# 12.3.1.3 Emergency Operation Time Interval calculation if no PMHF value is available

If the method of ISO 26262-5:2018, 9.4.3 is used, the criteria provided in ISO 26262-5:2018 9.4.3.13 is applicable.

# 12.3.1.4 Allocation of requirements after transition to safe state

If an item still provides some specified functions after reaching another safe state without timing restrictions, the ASIL capability of the remaining safety measures is evaluated. Relevant clauses of ISO 26262-5:2018 can be applied, including Clauses 8 and 9.

NOTE: For systematic faults, fault avoidance measures are comprehended as part of the development. If the effectiveness of these measures is quantified, then these measures can be taken into account for quantitative safety analysis (i.e. hardware architectural metrics of ISO 26262-5:2018, Clause 8 and PMHF or EEC of Clause 9).

# 12.4 Software development phase

# 12.4.1 Software fault avoidance and tolerance

Safety-related availability requirements for software can be addressed by two approaches: fault avoidance (12.4.2) and fault tolerance (12.4.3).

# 12.4.2 Software fault avoidance

The methods for fault avoidance are intended to reduce the overall occurrence of systematic faults. The necessary amount of fault avoidance can be achieved by developing software elements using ISO 26262-6.

# 12.4.3 Software fault tolerance

Techniques for fault tolerance try to keep the item operational despite the presence of software systematic faults. Some fault tolerant mechanisms are mentioned in ISO 26262-6:2018, 7.4.12, NOTE 2 and NOTE 3.

# 13 Remark on “Confidence in the use of software tools”

The process for determining confidence in the use of software tools, described in ISO 26262-8:2018, Clause 11, is divided into two steps:

1. 1st step: Evaluation of use cases of the tools
   The requirements for tool qualification are based on the determination of “Tool impact” (TI) and the “Tool error Detection” (TD) classes. TI represents the possibility that a malfunction of a particular software tool can introduce or fail to detect errors in a safety-related item or element being developed. TD represents the confidence in measures that prevent the software tool from malfunctioning and producing corresponding erroneous output, or in measures that detect that the software tool has malfunctioned and has produced corresponding erroneous output. TI and TD are used to determine the “Tool Confidence Level” (TCL).

TI and TD are determined based on the specific use-cases of the intended software tool. The evaluation of use-cases can be done independently from the specific tool itself. 2. 2nd step: Qualification of a software tool
If the 1st step results in a Tool Confidence Level TCL2 or TCL3, then qualification measures are means to ensure, that the user can rely on the correct functioning of a software tool and that the software tool is suitable to be used to support the activities or tasks required by the ISO 26262 series of standards. In this case, at least one of four qualification methods is recommended:

- Increased confidence from use.
- Evaluation of the tool development process.
- Validation of the software tool.
- Development in accordance with a safety standard.

The qualification method is applied to a specific software tool, its version and its environment. Therefore, ISO 26262-8:2018, 11.4.6.2, describes the documentation of:

- a unique identification and version number of the tool (a), and
- the configuration and environment for which the software tool is qualified (d).

Tool qualification often leads to high effort, especially in case of frequent changes of the tool or its version (e.g. in case of updates, patches, etc.), because the tool needs to be re-qualified for each new version. Re-qualification also applies to changes of the tool environment (e.g. the operating system or commonly used software libraries) which could have an impact on the tool output.

An alternative to tool qualification is to increase the probability to detect erroneous tool outputs by introducing additional measures into the product development process which uses the software tool. This would reduce the Tool error Detection classification to TD1. In this case the process flow is given in Figure 31:

Figure 31 — Tool qualification flow chart to achieve TCL1 classification of the tool

Since this alternative does not require the qualification of the specific software tool (2nd step), it is based only on the use-cases of the tool and can be performed independently of the specific tool, tool version and its environment.

This approach can lead to a higher initial and ongoing development effort because of the necessity to introduce additional measures for increasing the Tool error Detection (e.g. review of the tool output, additional test step, check by a subsequent tool, etc.). However, this typically results in a much lower tool qualification effort since the subsequent qualification steps can be omitted and in an ideal case this procedure is done only once.

The Tool Confidence Level is valid as long as the use-cases remain unchanged. In case of additional use-cases, the classification (1st step) is updated (impact analysis), which could result in the need for further measures to increase the Tool error Detection.

# 14 Guidance on safety-related special characteristics

# 14.1 General

This section gives guidance on safety-related special characteristics from their identification during the product development phase to the monitoring during the production phase.

Management of special characteristics is an established procedure to ensure that manufactured products or their elements provide the level of safety and quality required by customers. Therefore, the general approach in the ISO 26262 series of standards is compatible to the approach defined in established automotive quality management systems (see ISO 26262-2:2018, 5.4.5). The ISO 26262 series of standards has a specific focus on safety-related electrical, electronic and software elements of automotive products.

According to ISO 26262-7, the compliance with all safety-related special characteristics of items or elements during their production is necessary to achieve the functional safety of a product.

NOTE Special characteristics can be product characteristics or manufacturing process parameters.

The management of the safety-related special characteristics consists of:

- their identification during development;
- the specification of control measures used to control them during production planning; and
- the monitoring of their fulfilment during production.

The safety-related special characteristics are specified in ISO 26262-4:2018, 6.4.8.1 and ISO 26262-5:2018, 7.4.5.1, and are traceable in all of these three phases. Moreover, it is checked that each identified safety-related special characteristic has been suitably planned and controlled. The functional safety assessment can be used to provide evidence that the proper safety related special characteristics have been identified during the development phase. The production capability assessment is used to provide evidence that the production is capable of meeting the safety related special characteristics.

NOTE Relevant safety-related special characteristics could be exchanged between different organizations, e.g. customers and suppliers, to ensure traceability.

# 14.2 Identification of safety-related special characteristics

Safety-related special characteristics are identified both during product development and during production planning. To be able to identify the safety impact of the special characteristic on the item or element, information could be retrieved from the safety analyses reports according to ISO 26262-9.

NOTE 1 Production planning is initiated during the development.

NOTE 2 Not all special characteristics are safety-related.

Safety-related special characteristics can be identified at system, hardware, and software levels, and for production.

EXAMPLE 1 Calibration of an e-Motor Resolver offset is identified as a safety requirement for manufacturing during a system FMEA and an action is assigned to specify a safety-related special characteristic to be met during production for end-of-line testing, including storing calibration data and test results. The Process Control Plan specifies that e-Motor calibration is a safety-related special characteristic.

EXAMPLE 2 Minimum distance between two adjacent PINs ensuring electrical insulation is identified as a safety requirement for manufacturing during a component FMEA. An action is assigned to specify a safety-related special characteristic to be met during production of the hardware component, including test of electrical parameters, and an action is assigned to place a special characteristic symbol on the assembly drawing.

EXAMPLE 3 Correct selection of embedded software including calibration data for downloading to an ECU is identified as a safety-related special characteristic in a Process FMEA to be met during end-of-line programming of an ECU by comparing checksums.

EXAMPLE 4 Amount of solder paste deposited during the production process is identified as a safety-related special characteristic during a process FMEA to be met during production of the PCB, including control by vision systems.

# 14.3 Specification of the control measures of safety-related special characteristics

Once the safety-related special characteristics have been identified, criteria and requirements to control them during the production are specified to ensure functional safety of the item or element. Typically, the specification of the criteria and measures for controlling safety-related special characteristics includes:

- acceptable parameter range;
- EXAMPLE Acceptable current and voltage ranges.

evaluation or measurement technique including test ID;

EXAMPLE

Automatic Optical Inspection, End-Of-Line test, and In-Circuit Test.

- control strategy; and
- NOTE Control of samples could be statistically based or applied on all samples with a certain frequency. In this case sample size and frequency of the control are specified. These requirements can be given to external (e.g. suppliers) or internal production teams.
- Acceptance criteria.
- EXAMPLE Accepted tolerance for the width of a soldering patch

# 14.4 Monitoring of the safety-related special characteristics

Evidence of the planning and implementation of the control of safety-related special characteristics, including those from customers and suppliers, can be documented in the work products of ISO 26262-7:2018, 6.5.1 and 6.5.2.

# A (informative) Fault tree construction and applications

# A.1 General

The two most common techniques for analysing faults and failures of items and elements are FTA and FMEA. The FMEA is typically performed as an inductive (bottom up, see Figure A.1) approach focusing on the individual parts of the system, how they can fail and the impact of these failures on the system. The FTA is typically performed as a deductive (top down, see Figure A.2) approach starting with the undesired system behaviour and determining the possible causes of this behaviour. FTA includes coverage for combinations of multiple faults and events or situations which may lead to a hazard, while FMEA considers the effects of individual faults.

Figure A.1 — Illustration of FMEA, Bottom Up Approach

Figure A.2 — Illustration of FTA, Top Down Approach

The approaches are complementary as stated in ISO 26262-5:2018 7.4.3.1, Table 2 NOTE: “The level of detail of the analysis is commensurate with the level of detail of the design. Both methods can, in certain cases, be carried out at different levels of detail.” The “Cx” ovals of Figures A.1 and A.2 represent either hardware or software components. A typical approach is to use the FTA to analyse the hazards down to the component level. The failure modes of the components are then analysed from the bottom up using an FMEA to determine their failure modes and safety mechanisms to close out the bottom level of the fault tree. It is desirable to avoid duplicate work which would be caused by overlap between FTA modelling and FMEA. Preferably the results of the FMEA of serial system parts are fed as failure rates of the base events into the fault tree model.

NOTE 1: As stated in ISO 26262-9:2018, 7.4.2, the contribution of dependent failures is estimated on a qualitative basis because no general and sufficiently reliable method exists for quantifying such failures.

NOTE 2: Example standards for FMEA include JEP131A [3] and SAE J1739 [4], and for FTA IEC 61025 [5].

# A.2 Combining FTA and FMEA

Systems are composed of many parts and subparts. FTA and FMEA can be combined to provide the safety analysis with the right balance of top-down and bottom-up approach. Figure A.3 shows a possible approach to combining an FTA with an FMEA. In this figure, the basic events are derived from different FMEAs (labelled FMEA A-E within this example) which was performed at a lower level of abstraction (e.g. subpart, part or component level). Within this example, basic events 1 and 2 are fault effects as found in FMEA D, while no fault effects from FMEA B are used in the fault tree.

Figure A.3 — Illustration of a combination of FTA and FMEA

# Bibliography

1. IEC 61508 (all parts), Functional safety of electrical/electronic/programmable electronic safety-related systems
2. GSN COMMUNITY STANDARD VERSION 1, November 2011
3. JEDEC – JEP131A (May 2005), Potential Failure Mode and Effects Analysis (FMEA)
4. SAE-J1739_200901, Potential Failure Mode and Effects Analysis in Design (Design FMEA) and Potential Failure Mode and Effects Analysis in Manufacturing and Assembly Processes (Process FMEA) and Effects Analysis for Machinery (Machinery FMEA)
5. IEC 61025, ed. 2.0 — Procedures and Symbols for FTA
6. SAE J2980, Considerations for ISO 26262 ASIL Hazard Classification
7. ISO 26262-2:2018, Road vehicles — Functional safety — Part 2: Management of Functional Safety
8. ISO 26262-3:2018, Road vehicles — Functional safety — Part 3: Concept phase
9. ISO 26262-4:2018, Road vehicles — Functional safety — Part 4: Product development at the system level
10. ISO 26262-5:2018, Road vehicles — Functional safety — Part 5: Product development at the hardware level
11. ISO 26262-6:2018, Road vehicles — Functional safety — Part 6: Product development at the software level
12. ISO 26262-7:2018, Road vehicles — Functional safety — Part 7: Production, operation, service and decommissioning
13. ISO 26262-8:2018, Road vehicles — Functional safety — Part 8: Supporting processes
14. ISO 26262-9:2018, Road vehicles — Functional safety — Part 9: Automotive Safety Integrity Level (ASIL) oriented and safety-oriented analyses
15. ISO 26262-11:2018, Road vehicles — Functional safety — Part 11: Guideline on application of ISO 26262 to semiconductors
16. ISO 26262-12:2018, Road vehicles — Functional safety — Part 12: Adaptation of ISO 26262 for motorcycles
17. Convention on Road Traffic. Done at Vienna on 8 November 1968 including amendment 1, Economic Commission for Europe, Inland Transportation Committee, [viewed 2018-09-25] Available at: https://www.unece.org/fileadmin/DAM/trans/conventn/crt1968e.pdf
