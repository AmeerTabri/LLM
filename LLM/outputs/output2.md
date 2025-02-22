# 1 Scope

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>This document is intended to be applied to safety-related systems that include one or more electrical and/or electronic (E/E) systems and that are installed in series production road vehicles, excluding mopeds. This document does not address unique E/E systems in special vehicles such as E/E systems designed for drivers with disabilities.</p>
<p>NOTE Other dedicated application-specific safety standards exist and can complement the ISO 26262 series of standards or vice versa.</p>
<p>Systems and their components released for production, or systems and their components already under development prior to the publication date of this document, are exempted from the scope of this edition. This document addresses alterations to existing systems and their components released for production prior to the publication of this document by tailoring the safety lifecycle depending on the alteration. This document addresses integration of existing systems not developed according to this document and systems developed according to this document by tailoring the safety lifecycle.</p>
<p>This document addresses possible hazards caused by malfunctioning behaviour of safety-related E/E systems, including interaction of these systems. It does not address hazards related to electric shock, fire, smoke, heat, radiation, toxicity, flammability, reactivity, corrosion, release of energy and similar hazards, unless directly caused by malfunctioning behaviour of safety-related E/E systems.</p>
<p>This document describes a framework for functional safety to assist the development of safety-related E/E systems. This framework is intended to be used to integrate functional safety activities into a company-specific development framework. Some requirements have a clear technical focus to implement functional safety into a product; others address the development process and can therefore be seen as process requirements in order to demonstrate the capability of an organization with respect to functional safety.</p>
<p>This document does not address the nominal performance of E/E systems.</p>
<p>This document specifies the requirements for supporting processes, including the following:</p>
<ul>
<li>interfaces within distributed developments;</li>
<li>overall management of safety requirements;</li>
<li>configuration management;</li>
<li>change management;</li>
<li>verification;</li>
<li>documentation management;</li>
<li>confidence in the use of software tools;</li>
<li>qualification of software components;</li>
<li>evaluation of hardware elements;</li>
<li>proven in use argument;
— interfacing an application that is out of scope of ISO 26262; and
— integration of safety-related systems not developed according to ISO 26262.</li>
</ul>
<p>A provides an overview on objectives, prerequisites and work products of this document.</p>
    </body>
    </html>
    # 2 Normative references

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.</p>
<ul>
<li>ISO 26262-1, Road vehicles — Functional safety — Part 1: Vocabulary</li>
<li>ISO 26262-2:2018, Road vehicles — Functional safety — Part 2: Management of functional safety</li>
<li>ISO 26262-3:2018, Road vehicles — Functional safety — Part 3: Concept phase</li>
<li>ISO 26262-4:2018, Road vehicles — Functional safety — Part 4: Product development at the system level</li>
<li>ISO 26262-5:2018, Road vehicles — Functional safety — Part 5: Product development at the hardware level</li>
<li>ISO 26262-6:2018, Road vehicles — Functional safety — Part 6: Product development at the software level</li>
<li>ISO 26262-7:2018, Road vehicles — Functional safety — Part 7: Production, operation, service and decommissioning</li>
<li>ISO 26262-9:2018, Road vehicles — Functional safety — Part 9: Automotive Safety Integrity Level (ASIL)-oriented and safety-oriented analyses</li>
</ul>
    </body>
    </html>
    # 3 Terms and definitions

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>For the purposes of this document, the terms, definitions and abbreviated terms given in ISO 26262-1 apply.</p>
<p>ISO and IEC maintain terminological databases for use in standardization at the following addresses:</p>
<ul>
<li>IEC Electropedia: available at http://www.electropedia.org/</li>
<li>ISO Online browsing platform: available at https://www.iso.org/obp</li>
</ul>
    </body>
    </html>
    # 4 Requirements for compliance

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 4.1 Purpose

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>This clause describes how:</p>
<ul>
<li>a) to achieve compliance with the ISO 26262 series of standards;</li>
<li>b) to interpret the tables used in the ISO 26262 series of standards; and</li>
<li>c) to interpret the applicability of each clause, depending on the relevant ASIL(s).</li>
</ul>
    </body>
    </html>
    # 4.2 General requirements

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>When claiming compliance with the ISO 26262 series of standards, each requirement shall be met, unless one of the following applies:</p>
<ul>
<li>a) tailoring of the safety activities in accordance with ISO 26262-2 has been performed that shows that the requirement does not apply; or</li>
</ul>
<p>ISO 26262-8:2018(E)</p>
<p>b) a rationale is available that the non-compliance is acceptable and the rationale has been evaluated in accordance with ISO 26262-2.</p>
<p>Informative content, including notes and examples, is only for guidance in understanding, or for clarification of the associated requirement, and shall not be interpreted as a requirement itself or as complete or exhaustive.</p>
<p>The results of safety activities are given as work products. “Prerequisites” are information which shall be available as work products of a previous phase. Given that certain requirements of a clause are ASIL-dependent or may be tailored, certain work products may not be needed as prerequisites.</p>
<p>“Further supporting information” is information that can be considered, but which in some cases is not required by the ISO 26262 series of standards as a work product of a previous phase and which may be made available by external sources that are different from the persons or organizations responsible for the functional safety activities.</p>
    </body>
    </html>
    # 4.3 Interpretations of tables

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Tables are normative or informative depending on their context. The different methods listed in a table contribute to the level of confidence in achieving compliance with the corresponding requirement. Each method in a table is either:</p>
<ul>
<li>a) a consecutive entry (marked by a sequence number in the leftmost column, e.g. 1, 2, 3), or</li>
<li>b) an alternative entry (marked by a number followed by a letter in the leftmost column, e.g. 2a, 2b, 2c).</li>
</ul>
<p>For consecutive entries, all listed highly recommended and recommended methods in accordance with the ASIL apply. It is allowed to substitute a highly recommended or recommended method by others not listed in the table, in this case, a rationale shall be given describing why these comply with the corresponding requirement. If a rationale can be given to comply with the corresponding requirement without choosing all entries, a further rationale for omitted methods is not necessary.</p>
<p>For alternative entries, an appropriate combination of methods shall be applied in accordance with the ASIL indicated, independent of whether they are listed in the table or not. If methods are listed with different degrees of recommendation for an ASIL, the methods with the higher recommendation should be preferred. A rationale shall be given that the selected combination of methods or even a selected single method complies with the corresponding requirement.</p>
<p>NOTE A rationale based on the methods listed in the table is sufficient. However, this does not imply a bias for or against methods not listed in the table.</p>
<p>For each method, the degree of recommendation to use the corresponding method depends on the ASIL and is categorized as follows:</p>
<ul>
<li>— “++” indicates that the method is highly recommended for the identified ASIL;</li>
<li>— “+” indicates that the method is recommended for the identified ASIL; and</li>
<li>— “o” indicates that the method has no recommendation for or against its usage for the identified ASIL.</li>
</ul>
    </body>
    </html>
    # 4.4 ASIL-dependent requirements and recommendations

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The requirements or recommendations of each sub-clause shall be met for ASIL A, B, C and D, if not stated otherwise. These requirements and recommendations refer to the ASIL of the safety goal.</p>
<p>If ASIL decomposition has been performed at an earlier stage of development, in accordance with ISO 26262-9:2018, Clause 5, the ASIL resulting from the decomposition shall be met.</p>
<p>If an ASIL is given in parentheses in the ISO 26262 series of standards, the corresponding sub-clause shall be considered as a recommendation rather than a requirement for this ASIL. This has no link with the parenthesis notation related to ASIL decomposition.</p>
    </body>
    </html>
    # 4.5 Adaptation for motorcycles

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>For items or elements of motorcycles for which requirements of ISO 26262-12 are applicable, the requirements of ISO 26262-12 supersede the corresponding requirements in this document. Requirements of ISO 26262-2 that are superseded by ISO 26262-12 are defined in Part 12.</p>
    </body>
    </html>
    # 4.6 Adaptation for trucks, buses, trailers and semi-trailers

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Content that is intended to be unique for trucks, buses, trailers and semi-trailers (T&amp;B) is indicated as such.</p>
    </body>
    </html>
    # 5 Interfaces within distributed developments

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 5.1 Objectives

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The objectives of this clause are:</p>
<ul>
<li>a) to define the interactions and dependencies between customers and suppliers for development activities;</li>
<li>b) to describe the allocation of responsibilities; and</li>
<li>c) to identify the work products to be exchanged for distributed developments of an item and its elements.</li>
</ul>
    </body>
    </html>
    # 5.2 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The customer (e.g. vehicle manufacturer) and the suppliers for item or element developments jointly comply with the requirements specified in the ISO 26262 series of standards for distributed developments. Responsibilities are agreed between the customer and the suppliers for the concept, development, production, operation, service and decommissioning phases of the safety lifecycle. Subcontractor relationships are permitted. The customer has safety-related procedures concerning planning, execution and documentation for in-house item developments, therefore comparable procedures apply for co-operation with the supplier on distributed item developments. The same applies for item developments where the supplier has the full responsibility for functional safety.</p>
<p>NOTE 1 The Development Interface Agreement (DIA) aims to describe the roles and responsibilities between the customer and supplier. Consequently the safety planning by the customer and supplier is in line with the DIA.</p>
<p>NOTE 2 This clause is not relevant for the procurement which do not place any responsibility for safety on the supplier, including standard components and parts or development commissions.</p>
<p>NOTE 3 This note applies to T&amp;B: this clause is not relevant for body builder equipment being integrated into base vehicles. Clause 15 applies when integrating body builder equipment developed according to ISO 26262 into a base vehicle which is in scope of another standard. Clause 16 applies when body builder equipment developed according to another standard is integrated into a base vehicle developed according to ISO 26262.</p>
    </body>
    </html>
    # 12 Qualification of software components

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 12.1 Objectives

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The objective of the qualification of software components is to provide evidence for their suitability for re-use in items developed in compliance with the ISO 26262 series of standards.</p>
    </body>
    </html>
    # 12.2 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The use of qualified software components avoids re-development of existing software components with identical functionalities or properties or enables the use of general purpose commercial off-the-shelf (COTS) software.</p>
<p>NOTE Software components are understood to include source code, models, pre-compiled code, or compiled and linked software.</p>
<ol>
<li>Automotive SPICE® is an example of a suitable product available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by ISO of these products.</li>
</ol>
<p>EXAMPLE</p>
<p>Software components addressed by this clause include:</p>
<ul>
<li>software libraries from third-party suppliers [commercial off-the-shelf (COTS) software];</li>
<li>already existing SW components not developed according to ISO 26262;</li>
<li>in-house components already in use in electronic control units.</li>
</ul>
    </body>
    </html>
    # 12.3 Inputs to this clause

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 12.3.1 Prerequisites

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information shall be available:</p>
<ul>
<li>organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1; and</li>
<li>requirements of the software component (from an external source).</li>
</ul>
    </body>
    </html>
    # 12.3.2 Further supporting information

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information can be considered:</p>
<ul>
<li>design specification of the software component (from an external source); and</li>
<li>results of previous verification measures of the software component (from an external source).</li>
</ul>
    </body>
    </html>
    # 12.4 Requirements and recommendations

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 12.4.1 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>To be able to consider a software component as qualified, the following shall be available:</p>
<ol>
<li>the specification of the software component in accordance with 12.4.2.1;</li>
<li>evidence that the software component complies with its requirements in accordance with 12.4.2.2, 12.4.2.3, and 12.4.2.4;</li>
<li>evidence that the software component is suitable for its intended use in accordance with 12.4.3;</li>
<li>evidence that the software development process for the component is based on an appropriate national or international standard (e.g. ISO/IEC/IEEE 12207); and</li>
<li>a plan for the qualification of the software component.</li>
</ol>
<p>NOTE Some re-engineering activities can be performed in order to comply with this sub-clause in the case of previously developed software components.</p>
    </body>
    </html>
    # 12.4.2 Specification of software component qualification

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 12.4.2.1 The specification of the software component qualification shall include:

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <ol>
<li>the unique identification of the software component;</li>
<li>the maximum target ASIL of any safety requirement which might be violated if the software component performs incorrectly;</li>
<li>the activities that shall be carried out to qualify the software component;</li>
<li>the requirements of the software component;</li>
</ol>
<p>Requirements can include:</p>
<ul>
<li>functional requirements;</li>
<li>already known safety requirements;</li>
<li>accuracy of algorithm or numerical accuracy, where accuracy of algorithm considers procedural errors, which only provide approximate solutions and numerical accuracy considers rounding errors, resulting from computational inaccuracy, and truncation errors caused by the approximate representation of functions in the electronic control unit;</li>
<li>behaviour in the case of failure;</li>
<li>response time;</li>
<li>resource usage;</li>
<li>requirements on the runtime environment; and</li>
<li>behaviour in an overload situation (robustness).</li>
</ul>
<p>e) the requirements of the intended use of the software component;</p>
<p>f) the description of the configuration;</p>
<p>NOTE For software components that contain more than one software unit, the description of the configuration includes the unique identification and configuration of each software unit.</p>
<p>g) the description of required and provided interfaces and shared resources, if any;</p>
<p>h) the application manual, where appropriate;</p>
<p>i) the instructions for a correct software component integration;</p>
<p>NOTE This description includes configuration parameters of the development tools required to properly integrate and use the software component.</p>
<p>j) the reactions of the implemented functions under anomalous operating conditions; and</p>
<p>EXAMPLE Reaction to re-entrant calling of a non-re-entrant software function.</p>
<p>k) a description of known anomalies with corresponding workaround measures.</p>
    </body>
    </html>
    # 12.4.2.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>To provide evidence that a software component complies with its requirements the verification of this software component shall:</p>
<ul>
<li>show a requirement coverage in accordance with ISO 26262-6:2018, Clause 9;</li>
<li>NOTE This verification is primarily based on requirements-based tests. The results of requirements-based tests of the software component executed during its development or during previous integration tests can be used.</li>
</ul>
<p>EXAMPLE Application of a dedicated qualification test suite, analysis of all the tests already executed during the implementation and any integration of the software component.</p>
<p>cover both normal operating conditions and behaviour in the case of failure; and</p>
<ul>
<li>display no known errors that may lead to a violation of safety requirements allocated to this software component.</li>
</ul>
    </body>
    </html>
    # 12.4.2.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>This requirement applies to ASIL D, in accordance with 4.4: the structural coverage shall be measured in accordance with ISO 26262-6:2018, Clause 9, to evaluate the completeness of the test cases.</p>
    </body>
    </html>
    # 12.4.2.4 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The verification in accordance with 12.4.2.2, shall only be valid for an unchanged implementation of the software component.</p>
    </body>
    </html>
    # 12.4.2.5 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The qualification of a software component shall be documented including the following information:</p>
<ul>
<li>a) the unique identification of the software component;</li>
<li>b) the unique configuration of the software component;</li>
<li>c) the person or organization who carried out the qualification;</li>
<li>d) the environment used for qualification;</li>
<li>e) the results of the verification measures applied to qualify the software component; and</li>
<li>f) the maximum ASIL of the safety requirements allocated to the software component.</li>
</ul>
    </body>
    </html>
    # 12.4.3 Verification of qualification of a software component

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The results of qualification of a software component together with the validity of these results regarding the intended use of the software component shall be verified in accordance with Clause 9.</p>
    </body>
    </html>
    # 12.5 Work products

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 12.5.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Software component documentation resulting from requirement 12.4.2.1.</p>
    </body>
    </html>
    # 12.5.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Software component qualification report resulting from requirements 12.4.2.2 to 12.4.2.5.</p>
    </body>
    </html>
    # 12.5.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Software component qualification verification report resulting from requirement 12.4.3.</p>
    </body>
    </html>
    # 13 Evaluation of hardware elements

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.1 Objectives

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The objective of this clause is to ensure that the functional behaviour is adequate to meet the allocated safety requirements and therefore the risk of a violation of a safety goal or of a safety requirement, due to a systematic fault of the hardware element, is sufficiently low. Suitability for use based on random fault management is established by the integrator of the evaluated hardware element, at the next highest level of design integration.</p>
<p>NOTE 1 Meeting the requirements of the safety concept includes providing information on failure modes and failure mode distribution of the hardware element, suitable to conduct hardware failure analysis.</p>
<p>NOTE 2 It is not the objective of this clause to ensure the suitability of the hardware element concerning its robustness in its intended environmental conditions or its reliability. This is addressed for every hardware element within ISO 26262-5:2018, Clause 10.</p>
<p>In this clause, the use of the term “hardware element” refers either to COTS hardware components or parts, or to custom hardware components or parts, that:</p>
<ul>
<li>— are not originally developed or designed according to the ISO 26262 series of standards; and</li>
<li>— are considered to be safety-related within the context of the ISO 26262 compliant item or element into which they are to be integrated.</li>
</ul>
<p>More precisely, the evaluation of hardware elements is an alternative means of compliance with ISO 26262-5. The hardware elements eligible for evaluation can either be specific to an application.</p>
    </body>
    </html>
    # 13.2 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following goals are achieved by the evaluation of hardware elements:</p>
<ul>
<li>a) provide evidence that the hardware possesses an adequate functional performance and therefore is suitable to provide its intended function as required by the hardware design;</li>
<li>b) identification of new or confirmation of known failure modes and models (including the quantification of their distribution) by using appropriate tests (such as over limit test, accelerated test, etc.) or analyses;</li>
<li>c) identification of new or confirmation of known limits of use for hardware elements; and</li>
<li>d) provide an argument that the risk of a violation of a safety goal or the risk of a violation of a safety requirement due to systematic faults is sufficiently low.</li>
</ul>
<p>The evaluation of hardware elements is done in the context of a specific application. Within the evaluation of hardware elements the hardware element under consideration is classified either as class I, class II or class III element depending on its properties. These classes reflect the difficulty of the verification of the safety-related functionality and the role of the hardware element within the safety concept.</p>
<p>Depending on its class, different requirements to evaluate the hardware element are given. As a first step the relevant requirements for the hardware element are specified and its safety related failure modes are identified.</p>
<p>For the evaluation of class I elements it is sufficient to test the hardware element into which the evaluated hardware elements are integrated according to ISO 26262-5:2018, Clause 10. The evaluation of class II elements can be done with a combination of tests and analyses. For the evaluation of class III elements, in addition to the evaluation activities necessary for a class II element, an argument is added showing that the risk of a safety goal violation or the risk of a safety requirement violation is sufficiently low.</p>
    </body>
    </html>
    # 13.3 Inputs to this clause

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.3.1 Prerequisites

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information shall be available:</p>
<ul>
<li>— organization-specific rules and processes for functional safety in accordance with ISO 26262-2:2018, 5.5.1;</li>
<li>— the safety requirements related to the considered hardware element;</li>
<li>— criteria for design verification (analysis and tests) in accordance with ISO 26262-5:2018, Clause 6; and</li>
<li>— the manufacturer's hardware element specification, or, if unavailable, the assumptions on hardware element specification (from an external source).</li>
</ul>
    </body>
    </html>
    # 13.3.2 Further supporting information

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information can be considered:</p>
<ul>
<li>— further supporting information for the phases of the safety lifecycle where the evaluation of hardware elements is applied.</li>
</ul>
    </body>
    </html>
    # 13.4 Requirements and recommendations

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.1 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.1.1 Classification of the evaluated hardware element

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The hardware element shall be classified as one of the following classes:</p>
<p>a) Class I if:</p>
<ul>
<li>the element has at the maximum a few states which can be fully characterized, tested and analysed from a safety perspective;</li>
<li>safety related failure modes can be identified and evaluated without knowledge about details of the implementation and the production process of the element; and</li>
<li>the element has no internal safety mechanisms which are relevant for the safety concept to control or detect internal failures.</li>
</ul>
<p>NOTE This does not include safety mechanisms that monitor properties outside of the element.</p>
<p>EXAMPLE Resistor, capacitor, transistor, diode, quartz, resonator.</p>
<p>b) Class II if:</p>
<ul>
<li>the element has e.g. few operating modes, small value ranges, few parameters and can be analysed from safety perspective without knowing implementation details;</li>
<li>available documentation allows valid assumptions supporting evaluation of systematic faults by testing and analysis without knowledge about details of the implementation and the production process of the element; and</li>
</ul>
<p>EXAMPLE Datasheets, user manuals, application notes.</p>
<ul>
<li>the element has no internal safety mechanisms which are relevant for the safety concept to control or detect internal failures.</li>
</ul>
<p>NOTE This does not include safety mechanisms that monitor properties outside of the element.</p>
<p>EXAMPLE Fuel pressure sensor, temperature sensor, stand-alone Analog Digital Converter (ADC) without internal safety mechanisms relevant for the safety concept.</p>
<p>c) Class III if:</p>
<ul>
<li>the element has e.g. many operating modes, wide value ranges or many parameters which are impossible to analyse without knowing implementation details,</li>
<li>sources for systematic faults can only be understood and analysed by knowledge about detailed implementation, the development process and/or the production process, or</li>
<li>the element has internal safety mechanisms which are relevant for the safety concept to control or detect internal failures.</li>
</ul>
<p>EXAMPLE Microprocessor, microcontroller, Digital Signal Processor (DSP).</p>
    </body>
    </html>
    # 13.4.1.2 The requirements for the hardware element resulting from the allocated safety requirements

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>and the safety concept shall be specified.</p>
<p>NOTE For class I elements this usually coincides with the specification of the hardware element, e.g. nominal value and tolerances for a resistor.</p>
    </body>
    </html>
    # 13.4.1.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The failure modes or faults of the hardware element and their distribution concerning random hardware faults shall be identified.</p>
    </body>
    </html>
    # 13.4.1.4 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The safety related failure modes or faults of the hardware element shall be identified. The analysis shall provide evidence that the requirements resulting from ISO 26262-5:2018, 7.4.3, Clauses 8 and 9 are met.</p>
    </body>
    </html>
    # 13.4.2 Evaluation of class I hardware elements

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Due to the simplicity of the functionality of a class I element, it does not need to be evaluated by itself; the hardware element into which it is integrated shall be developed in compliance with ISO 26262.</p>
    </body>
    </html>
    # 13.4.3 Evaluation of class II hardware elements

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.3.1 Methods for evaluation

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The evaluation of the class II hardware element shall be carried out using an appropriate selection of analysis and testing.</p>
    </body>
    </html>
    # 13.4.3.2 Evaluation plan

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>An evaluation plan shall be developed and shall describe:</p>
<ul>
<li>a unique identification and version of the hardware element;</li>
<li>a specification of the environment in which the hardware element is intended to be used;</li>
<li>the evaluation strategy and the rationale;</li>
</ul>
<p>NOTE The strategy includes: analysis, necessary tests and step by step description.</p>
<ul>
<li>the necessary tools and equipment according to the strategy;</li>
<li>the party responsible for carrying out the evaluation; and</li>
<li>the pass and fail criteria for the evaluation of a hardware element.</li>
</ul>
    </body>
    </html>
    # 13.4.3.3 Evaluation argument

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.3.3.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A comprehensive argument that the functional performance of the hardware element complies with its specification and it is adequate for its intended use, according to the hardware design, shall be made available.</p>
<p>NOTE The required performances encompass behaviour when it is subjected to the established normal environmental conditions and to the environmental conditions in combination with an assumed failure initiating event.</p>
    </body>
    </html>
    # 13.4.3.3.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The comprehensive argument of 13.4.3.3.1 shall be based on a combination of the following types of information:</p>
<ul>
<li>analytical methods and assumptions used;</li>
<li>data from operational experience; and</li>
<li>existing testing results.</li>
</ul>
    </body>
    </html>
    # 13.4.3.3.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A rationale for each assumption, including extrapolations, shall be given.</p>
    </body>
    </html>
    # 13.4.3.4 Evaluation by analyses

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.3.4.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The result of the analysis shall be provided in a form that is comprehensive and can be verified by persons who are qualified in the relevant engineering or scientific disciplines.</p>
<p>NOTE Analytical methods that can be used include design verification methods, e.g. extrapolations, mathematical models, damage analysis or similar methods, and process gap analysis in order to show sufficient evidence for systematic failure avoidance will be available.</p>
    </body>
    </html>
    # 13.4.3.4.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The analysis shall consider all the environmental conditions to which the hardware element is exposed, the limits of these conditions and other additional stresses related to operation (e.g. expected switch cycles, charging and discharging, long turn-off times).</p>
    </body>
    </html>
    # 13.4.3.5 Evaluation by testing

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.3.5.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A test plan shall be developed which contains the following information:</p>
<ul>
<li>a) a description of the functions of the hardware element;</li>
<li>b) allocated safety requirements;</li>
<li>c) the specification and sequence of tests to be conducted;</li>
<li>d) the traceability between tests and safety requirements;</li>
<li>e) the requirements for assembly and connections;</li>
<li>f) the operating and environmental conditions to be simulated;</li>
<li>g) number of elements tested;</li>
<li>h) pass and fail criteria;</li>
<li>i) environmental parameters to be measured; and</li>
<li>j) requirements for the testing equipment, including accuracy.</li>
</ul>
    </body>
    </html>
    # 13.4.3.5.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The test to verify robustness of the hardware element under evaluation against external stresses shall be done in accordance with ISO 26262-5:2018, 10.4.6.</p>
<p>EXAMPLE This specification can be based on the ISO 16750 series of standards or equivalent company standards.</p>
    </body>
    </html>
    # 13.4.3.5.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The test shall be conducted as planned and the resulting test data shall be made available.</p>
    </body>
    </html>
    # 13.4.3.5.4 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The integration into the ISO 26262 compliant element shall comply with ISO 26262-5:2018, Clause 10 or ISO 26262-4:2018, Clause 7.</p>
    </body>
    </html>
    # 13.4.3.6 Evaluation report

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.3.6.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The evaluation report shall state whether the hardware element has passed or failed the evaluation, based on the performed analyses and testing, with respect to the safety requirements specified and allocated to it, including its operating range and conditions.</p>
<p>NOTE The evaluation report can consist of a set of documents that includes reports on findings and notes on interpretation.</p>
    </body>
    </html>
    # 13.4.3.6.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The evaluation report shall be verified in accordance with Clause 9.</p>
    </body>
    </html>
    # 13.4.4 Evaluation of class III hardware elements

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.4.4.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Class III hardware elements should be developed in compliance with ISO 26262.</p>
<p>NOTE This means that the “evaluation of class III elements” is not the preferred approach and therefore the next version of the hardware element is planned to be developed in compliance with ISO 26262.</p>
    </body>
    </html>
    # 13.4.4.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>For the evaluation of the class III hardware elements the requirements stated in 13.4.3 shall be met.</p>
    </body>
    </html>
    # 13.4.4.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Additional measures shall be provided to argue that the risk of a safety goal violation or the risk of a safety requirement violation due to systematic faults is sufficiently low.</p>
<p>NOTE 1 Depending on the combination of arguments provided, the result of the hardware evaluation shows that using the class III element in the context of the given application is safe. However the argument is not valid for all applications.</p>
<p>NOTE 2 Measures can include but are not limited to:</p>
<ul>
<li>a) verifiability of the safety related functionality;</li>
<li>b) field experience/“well-trusted component”; NOTE Field experience can be used as a partial supporting argument for hardware evaluation. For a full proven-in-use argument, ISO 26262-8:2018, Clause 14 is followed instead of this clause.</li>
<li>c) supervision by an independent diverse element with the capability to detect the safety related failure modes; NOTE A Dependent Failure Analysis compliant with ISO 26262-9:2018, Clause 7, shows the independence.</li>
<li>d) development compliant with a different safety standard with a comparable integrity level.</li>
</ul>
    </body>
    </html>
    # 13.5 Work products

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 13.5.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Hardware element evaluation plan resulting from requirement 13.4.3.2.</p>
    </body>
    </html>
    # 13.5.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Hardware element test plan if applicable, resulting from requirement 13.4.3.5.1.</p>
    </body>
    </html>
    # 13.5.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Hardware element evaluation report for hardware elements resulting from requirements 13.4.1.1, 13.4.3.6 and 13.4.4.3, if applicable.</p>
    </body>
    </html>
    # 14 Proven in use argument

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 14.1 Objectives

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The objective of this clause is to provide guidance for a proven in use argument. A proven in use argument is an alternate means of compliance with the ISO 26262 series of standards that may be used in the case of reuse of existing items or elements when field data is available.</p>
    </body>
    </html>
    # 14.2 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A proven in use argument can be applied to any type of product whose definition and conditions of use are identical to or have a very high degree of commonality with a product that is already released and in operation. It can also be applied to any work product related to such products.</p>
<p>NOTE 1 Proven in use argument is not inter-changeability: one product, with alternate design or implementation, that is intended to replace a proven in use product cannot be considered to be proven in use because it fulfils the original functional requirements, unless this product meets the criteria specified in this clause.</p>
<p>An item or an element, such as system, function, hardware or whole software product, can be a candidate for a proven in use argument. A candidate can also refer to a work product such as a technical safety concept.</p>
<p>The motivation for using the argument for proven in use includes:</p>
<ul>
<li>a) an automotive application in commercial use intended to be partly or completely carried over to another target, or</li>
<li>b) an Electronic Control Unit (ECU) in operation intended to implement an additional function, or</li>
<li>c) a candidate being in the field prior to the release of the ISO 26262 series of standards, or</li>
<li>d) a candidate being used in other safety-related industries, or</li>
<li>e) a candidate being a widely used COTS product not necessarily intended for automotive applications.</li>
</ul>
<p>The proven in use argument is substantiated by appropriate documentation on the candidate, configuration management and change management records, and field data regarding safety-related incidents.</p>
<p>Once a candidate has been defined (see 14.4.3) with the expected proven in use credit (see 14.4.2), two important criteria need to be considered when preparing a proven in use argument:</p>
<ul>
<li>— the relevance of field data during the previous evaluation period of the candidate (see 14.4.5); and</li>
<li>— the changes, if any, that could have impacted the candidate since its previous evaluation period (see 14.4.4).</li>
</ul>
<p>NOTE 2 With regard to the relevance of field data, the proven in use argument is intended to address systematic and random failures of the candidate; it does not address failures related to ageing of the candidate.</p>
<p>Using proven in use items or elements does not exempt those items or elements from the following project-dependent safety management activities:</p>
<ul>
<li>— the proven in use credit is described in the safety plan; and</li>
<li>— the data and work products resulting from the proven in use argument are part of the safety case and subject to confirmation measures.</li>
</ul>
    </body>
    </html>
    # 14.3 Inputs to this clause

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 14.3.1 Prerequisites

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information shall be available:</p>
<ul>
<li>— regarding the intended use of a candidate:</li>
</ul>
<p>— foreseeable operational situation and intended operating modes and interfaces;</p>
<p>— regarding the previous use of a candidate:</p>
<p>— field data from the service period (from an external source).</p>
    </body>
    </html>
    # 14.3.2 Further supporting information

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information can be considered regarding the previous use of a candidate:</p>
<p>— safety case in accordance with ISO 26262-2:2018, 6.5.4.</p>
<p>NOTE For a candidate not developed in accordance with the ISO 26262 series of standards (e.g. COTS products, candidates developed under a safety standard other than ISO 26262, such as IEC 61508 or RTCA DO-178C), some work products of the safety case may not be available, in which case they are substituted by available data resulting from the development of the candidate.</p>
    </body>
    </html>
    # 14.4 Requirements and recommendations

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 14.4.1 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following sub-clauses refer to the ASILs applicable to the future use of the candidate.</p>
    </body>
    </html>
    # 14.4.2 Proven in use credit

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 14.4.2.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A proven in use credit shall be used only when the candidate complies with 14.4.2 to 14.4.5.</p>
    </body>
    </html>
    # 14.4.2.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The proven in use credit resulting from a proven in use argument shall be planned in accordance with ISO 26262-2:2018, 6.4.5.</p>
    </body>
    </html>
    # 14.4.2.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The proven in use credit shall be limited to the safety lifecycle sub-phases and activities covered by the proven in use argument of the candidate.</p>
    </body>
    </html>
    # 14.4.2.4 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Integration measures of proven in use elements in an item or element shall be carried out at the appropriate level in accordance with ISO 26262-4:2018, Clause 8.</p>
<p>EXAMPLE The hardware of an ECU has a satisfactory field history and is intended to be 100 % carried over to a new application. The proven in use credit can be applied to the sub-phases and activities of development of this hardware element. Similarly, if the software is a 100 % carryover with a satisfactory service history, then the proven in use credit can also be applied to the software sub-phases and activities.</p>
    </body>
    </html>
    # 14.4.2.5 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Safety validation of an item which embeds proven in use elements shall be carried out in accordance with ISO 26262-4:2018, Clause 9.</p>
    </body>
    </html>
    # 14.4.2.6 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The confirmation measures of an item that embeds proven in use elements shall consider the proven in use arguments and related data in accordance with ISO 26262-2:2018, 6.4.9 and 6.4.10.</p>
    </body>
    </html>
    # 14.4.2.7 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Any modification to a proven in use item or element shall comply with 14.4.4 for the corresponding proven in use credit to be maintained.</p>
<p>NOTE This clause applies to any type of modification including those initiated as a result of a safety-related incident.</p>
    </body>
    </html>
    # 14.4.3 Minimum information on candidate

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A description of the candidate and its previous use shall be available, and includes:</p>
<ul>
<li>a) the identification and traceability of the candidate with a catalogue of internal elements or components, if any;</li>
<li>b) the corresponding fit, form and function requirements that describe, if applicable, interface and environmental, physical and dimensional, functional and performance characteristics of the candidate; and</li>
<li>c) the safety requirements of the candidate in the previous use and the corresponding ASILs, if available.</li>
</ul>
    </body>
    </html>
    # 14.4.4 Analysis of modifications to the candidate

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 14.4.4.1 Proven in use candidates

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Modifications to candidates and their environment shall be identified in accordance with 14.4.4.2 to 14.4.4.3.</p>
<p>NOTE 1 Modifications to candidates address design changes and implementation changes. Design changes can result from modification of requirements, functional enhancements or performance enhancement. Implementation changes do not affect specification or performance of the candidate but only its implementation features. Implementation changes can result from software corrections or use of new development or production tools.</p>
<p>NOTE 2 Changes to configuration data or calibration data are considered as modifications to the candidate when they impact its behaviour with regard to the violation of the safety goals.</p>
<p>NOTE 3 Changes to the environment of a candidate can result from use of this candidate in a new type of application with different safety goals or requirements, its installation in a new target environment (e.g. variant of vehicle, range of environmental conditions) or the upgrading of the components interacting with it or located in its vicinity.</p>
    </body>
    </html>
    # 14.4.4.2 Modifications to items introduced for a future application

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Modifications to items and their environment introduced for the purpose of a future application shall comply with ISO 26262-2:2018, 6.4.3.</p>
    </body>
    </html>
    # 14.4.4.3 Modifications to elements introduced for a future application

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Modifications to elements and their environment introduced for the purpose of a future application within a different item shall comply with ISO 26262-2:2018, 6.4.4.</p>
    </body>
    </html>
    # 14.4.4.4 Modifications to candidate independent of future application

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Modifications to a candidate introduced after its evaluation period, independent of future applications, shall provide evidence that the proven in use status remains valid.</p>
    </body>
    </html>
    # 14.4.5 Analysis of field data

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 14.4.5.1 Configuration management and change management

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Evidence shall be provided that the candidate has been kept under configuration management and change management during and after its evaluation period so that the current status of the candidate can be established.</p>
    </body>
    </html>
    # 14.4.5.2 Target values for proven in use

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>NOTE When any ASIL is not yet assigned to the candidate, ASIL D target is selected conservatively.</p>
    </body>
    </html>
    # 14.4.5.2.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The rationale for the calculation of the evaluation period of the candidate shall be available.</p>
    </body>
    </html>
    # 14.4.5.2.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The evaluation period of the candidate shall result from the addition of the observation period of all the specimens taken in reference in accordance with 14.4.5.2.3.</p>
    </body>
    </html>
    # 14.4.5.2.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The observation period of each specimen with the same specification and realization as the candidate and running in a vehicle shall exceed the average yearly vehicle operating time before being considered in the analysis of the evaluation period of the candidate.</p>
    </body>
    </html>
    # 14.4.5.2.4 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>For a proven in use status to be obtained by the candidate, its evaluation period shall demonstrate compliance with each safety goal that can be violated by the candidate in accordance with Table 6 with a single-sided lower confidence level of 70 % (using a chi-square distribution).</p>
<p>NOTE 1 For the purpose of the proven in use argument, an observable incident means a failure that is reported to the manufacturer and caused by the candidate with the potential to lead to the violation of a safety goal.</p>
<p><strong>Table 6 — Limits for observable incident rate</strong>
|ASIL|Observable incident rate|
|---|---|
|D|&lt;10−9/h|
|C|&lt;10−8/h|
|B|&lt;10−8/h|
|A|&lt;10−7/h|</p>
<p>NOTE 2 The character and rate of observable incidents are interpreted when analysing the potential violation of the safety goals in the field.</p>
<p>NOTE 3 Table 7 gives an example of the required minimum service period without observable incident which is necessary to achieve 70 % confidence.</p>
<p><strong>Table 7 — Targets for minimum evaluation period of candidate</strong>
|ASIL|Minimum evaluation period without observable incident|
|---|---|
|D|1,2 × 109 h|
|C|1,2 × 108 h|
|B|1,2 × 108 h|
|A|1,2 × 107 h|</p>
<p>NOTE 4 If observable incidents are found in the collected data of the specimens, the necessary minimum evaluation period, tservice, can be adjusted as follows:</p>
<p>tservice = MTTF × (χCL;2 f + 2)2t2</p>
<p>where</p>
<ul>
<li>CL is the confidence level as an absolute value (e.g. 0,7 for 70 %);</li>
<li>tMTTF is the mean time to failure (1/failure rate);</li>
<li>f is the number of safety-related incidents;</li>
<li>(χα, ν) is the chi-squared distribution with error probability α and ν degrees of freedom.</li>
</ul>
    </body>
    </html>
    # 14.4.5.2.5 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The application of the proven in use credit may be anticipated provisionally, before a proven in use status is obtained (in accordance with 14.4.5.2.4). In this case, the evaluation period of the candidate shall demonstrate compliance with each safety goal that can be violated by the candidate in accordance with Table 8 with a single sided lower confidence level of 70 % (using a chi-square distribution).</p>
<p><strong>Table 8 — Limits for observable incident rate (interim period)</strong>
|ASIL|Observable incident rate|
|---|---|
|D|&lt;3 × 10−9/h|
|C|&lt;3 × 10−8/h|
|B|&lt;3 × 10−8/h|
|A|&lt;3 × 10−7/h|</p>
    </body>
    </html>
    # 14.4.5.2.6 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>In the case of any observed incident in the field during the interim period described in 14.4.5.2.5, the following shall be complied with:</p>
<ul>
<li>to stop using Table 8 for the observable incident rate and to use alternatively</li>
<li>to provide evidence that the root cause of the observed incident is fully identified and eliminated in accordance with the ISO 26262 series of standards, and to keep on counting the cumulated hours for the candidate, to reset the counter of cumulated hours for this specific root cause and to record this evidence in the safety case.</li>
</ul>
    </body>
    </html>
    # 14.4.5.2.7 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>In the case of a candidate with a non-constant failure rate, additional measures shall be applied for the proven in use argument, for instance in the case of damage resulting from fatigue.</p>
<p>NOTE Those measures apply to candidates with failure rates significantly dependent on factors such as wear, ageing or operating hours regarding the lifetime of the item. They can include dedicated endurance tests, or a longer observation period.</p>
    </body>
    </html>
    # 14.4.5.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Field problems</p>
<p>The problem reporting system shall ensure that any observed incident with potential safety impact caused by the candidate in the field, is recorded and retrievable during the period of operation of the candidate (see ISO 26262-2:2018, 7.4.2.3).</p>
    </body>
    </html>
    # 14.5 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Work products</p>
    </body>
    </html>
    # 14.5.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Description of candidate for proven in use argument resulting from requirement 14.4.3.</p>
    </body>
    </html>
    # 14.5.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Proven in use analysis reports resulting from requirements 14.4.4 to 14.4.5.</p>
    </body>
    </html>
    # 15 Interfacing an application that is out of scope of ISO 26262

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 15.1 Objectives

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>This clause applies to T&amp;B, where the objective is to achieve confidence that an application that is out of scope of ISO 26262 is not able to violate the safety goals of the base vehicle or item that has been developed in accordance with the ISO 26262 series of standards.</p>
    </body>
    </html>
    # 15.2 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The application of this clause is intended for commercial vehicle business models where a company assembles or integrates a complete vehicle that is not in scope of ISO 26262 but to which another standard applies. The relationship between the application and item according to ISO 26262 is depicted in Figure 5.</p>
<p>Figure 5 — Item developed according to ISO 26262 used in scope of another standard</p>
<p>EXAMPLE 1</p>
<p>A body builder, as an integrator, assembles a complete vehicle by integrating a base vehicle developed according to the ISO 26262 series of standards with body builder equipment developed according to the Machinery Directive.</p>
<p>EXAMPLE 2</p>
<p>A manufacturer of agricultural equipment integrates a brake system developed according to the ISO 26262 series of standards into agricultural equipment developed according to standards for machinery for agriculture and forestry.</p>
    </body>
    </html>
    # 15.3 Inputs to this clause

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 15.3.1 Prerequisites

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information shall be available:</p>
<ul>
<li>item definition in accordance with ISO 26262-3:2018, 5.5.1</li>
</ul>
    </body>
    </html>
    # 15.3.2 Further supporting information

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>None.</p>
    </body>
    </html>
    # 15.4 Requirements and recommendations

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 15.4.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The requirements in 15.4 shall be applied to T&amp;B.</p>
    </body>
    </html>
    # 15.4.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The base vehicle manufacturer or supplier of an item or element shall communicate information to the integrator identifying the modifiable systems and components and the permitted system safety limits/requirements of the modifications.</p>
    </body>
    </html>
    # 15.4.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The base vehicle manufacturer or supplier of an item shall communicate the safety measures required to be applied by the integrator.</p>
<p>NOTE 1 It is assumed that the integrator has the necessary capability to realize the safety measures.</p>
<p>EXAMPLE 1</p>
<p>Criteria for the capability of an integrator can be:</p>
<ul>
<li>compliance with other safety standards,</li>
<li>an appropriate safety culture, and</li>
<li>an established quality management system.</li>
</ul>
<p>NOTE 2 The base vehicle manufacturer or supplier of an item or element makes assumptions about intended integrator use cases together with the safety requirements. For exceptions, the integrator contacts the base vehicle manufacturer or supplier of the item or element for safety requirements.</p>
<p>EXAMPLE 2 A body builder contacts a base vehicle manufacturer to request PTO activation during driving. The body builder uses ISO 13849 and both agree on an ASIL to ISO 13849. The base vehicle manufacturer communicates the safety requirements (with ASIL) regarding the PTO request, the body builder complies with these requirements (with agreed Performance Level). The base vehicle manufacturer enables the requested PTO function for the body builder.</p>
    </body>
    </html>
    # 15.5 Work products

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 15.5.1 Base Vehicle Manufacturer or Supplier guideline resulting from requirements 15.4.2 and 15.4.3.

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 16 Integration of safety-related systems not developed according to ISO 26262

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 16.1 Objectives

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>This clause applies to T&amp;B, where the objective is to achieve confidence that a system or component that is not developed according the ISO 26262 series of standards satisfies the required level of functional safety needed for the integration into an item developed according to the ISO 26262 series of standards.</p>
    </body>
    </html>
    # 16.2 General

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The application of this clause is intended for commercial vehicle business models where a company which follows ISO 26262 integrates a system or component which is not developed according to the ISO 26262 series of standards, but which has been developed according to another standard. The relationship between the application and item according to the ISO 26262 series of standards is depicted in Figure 6.</p>
<p>Figure 6 — Integration of a system developed according to another standard</p>
<p>NOTE 1 Since this business model can demand higher effort and development costs for the integrator due to additional safety activities, a conventional ISO 26262 development is favoured.</p>
<p>NOTE 2 A business model for commercial vehicles could be series production with low quantities.</p>
<p>NOTE 3 Another standard could be the Machinery Directive including IEC 61508, ISO 13849 and ISO 25119. Company specific processes could also be used for the integration.</p>
    </body>
    </html>
    # 16.3 Inputs to this clause

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 16.3.1 Prerequisites

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The following information shall be available:</p>
<ul>
<li>item definition in accordance with ISO 26262-3:2018, 5.5.1.</li>
</ul>
<p>NOTE 1 The Item definition relates to the system or array of systems on the integrator side, that includes the system or component not developed according to ISO 26262.</p>
<p>NOTE 2 An integrator of such systems or components can be the base vehicle manufacturer.</p>
    </body>
    </html>
    # 16.3.2 Further supporting information

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>None.</p>
    </body>
    </html>
    # 16.4 Requirements and recommendations

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 16.4.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The requirements in 16.4 shall be applied to T&amp;B.</p>
    </body>
    </html>
    # 16.4.2 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>A rationale shall be given in the integrator safety case that justifies the application of this clause.</p>
<p>EXAMPLE The supplier follows the safety standard ISO 13849.</p>
    </body>
    </html>
    # 16.4.3 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The integrator shall define the criteria to argue that the safety-related system that has been developed to another safety standard meets the required level of functional safety.</p>
<p>EXAMPLE 1 A mapping between ASIL and PL (Performance Level as used in ISO 13849).</p>
<p>NOTE The criteria address the design process, the product design, qualification measures and approval process.</p>
<p>EXAMPLE 2 Comparison of requirements regarding applied methods and requested failure rates of different safety standards.</p>
    </body>
    </html>
    # 16.4.4 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>The integrator and supplier shall agree on the relevant set of measures to verify that the criteria are met.</p>
<p>EXAMPLE A set of measures can be:</p>
<ul>
<li>availability of the specification for the system to be integrated;</li>
<li>evidence that the system to be integrated complies with its requirements by test report;</li>
<li>structured design analysis for systematic design faults by FMEA, FTA, application of established design pattern/configurations;</li>
<li>evidence that the system to be integrated is suitable for its intended use;</li>
<li>evidence that the product release for the component is based on an adequate approval process by PPAP (Production Part Approval Process);</li>
<li>design verification/validation testing by highly accelerated life testing, environmental testing, testing beyond specification limits, robustness testing; and</li>
<li>analysis of field data.</li>
</ul>
    </body>
    </html>
    # 16.5 Work products

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        
    </body>
    </html>
    # 16.5.1 ???

    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <p>Safety rationale resulting from requirements 16.4.2 to 16.4.4.</p>
    </body>
    </html>
    