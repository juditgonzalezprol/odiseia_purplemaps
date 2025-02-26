import streamlit as st
import pandas as pd

st.set_page_config(page_title="Terms and Conditions", layout="wide")

# Bloque de CSS para forzar color y fondo
st.markdown(
    """
    <style>
    * {
            font-family: 'Google Sans', sans-serif;
    }
    /* Fondo blanco para la app */
    .stApp {
        background-color: #ffffff !important;
    }

    /* Forzar color de texto en toda la interfaz */
    html, body, [class*="css"]  {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Aquí ya puedes mostrar tu texto sin que se pinte de rosa
st.markdown(
    """
    ## En esta página se incluyen los términos y condiciones, así como la política de privacidad respecto del servicio PurpleMaps
    
    # TERMS AND CONDITIONS
    Last updated February 25, 2025

    ### AGREEMENT TO OUR LEGAL TERMS

    We are Purple Maps ("Company," "we," "us," or "our"), a company registered in Spain at Calle Mayor, 10, Madrid, Madrid 28013. Our VAT number is N/A.

    We operate the website https://odiseiapurplemaps.streamlit.app/ (the "Site"), the mobile application Purple Maps (the "App"), as well as any other related products and services that refer or link to these legal terms (the "Legal Terms") (collectively, the "Services").

    Our platform is a comprehensive tool designed to empower and connect communities through a network of designated “Violet Points.” It offers the following key functionalities:

    - Interactive Violet Points Map: View a dynamic map displaying available Violet Points, allowing users to easily locate assistance and support services.
    - Alerts System: Search for, add, and manage alerts related to important events or updates at Violet Points, ensuring users are informed in real time.
    - 24/7 AI-Powered Chat Support: Access around-the-clock chat support, where an AI-driven assistant is specifically trained to function as a Violet Point guide. This assistant provides general legal information and support on an informational basis only and is not a substitute for professional legal counsel.
    - Comprehensive Documentation and Terms: Gain full access to detailed documentation and clear terms of use, outlining user rights, responsibilities, and the operational framework of the platform.
    - Volunteer and Management Requests: Submit applications to become a Violet Point manager or volunteer, enabling proactive community engagement and support.

    Our platform is developed with a strong commitment to transparency, user safety, and legal compliance. In particular, our AI-driven chat support is designed and operated in accordance with the latest European Union regulations on artificial intelligence, ensuring ethical and secure practices. Users are encouraged to review our documentation to fully understand the scope and limitations of the services provided. By using our platform, you benefit from a robust, real-time toolset aimed at enhancing community safety, information sharing, and active participation in the management and support of Violet Points.

    You can contact us by phone at +34 900 123 456, email at contact@purplemaps.com, or by mail to Calle Mayor, 10, Madrid, Madrid 28013, Spain.

    These Legal Terms constitute a legally binding agreement made between you, whether personally or on behalf of an entity ("you"), and Purple Maps, concerning your access to and use of the Services. You agree that by accessing the Services, you have read, understood, and agreed to be bound by all of these Legal Terms. IF YOU DO NOT AGREE WITH ALL OF THESE LEGAL TERMS, THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE SERVICES AND YOU MUST DISCONTINUE USE IMMEDIATELY.

    Supplemental terms and conditions or documents that may be posted on the Services from time to time are hereby expressly incorporated herein by reference. We reserve the right, in our sole discretion, to make changes or modifications to these Legal Terms from time to time. We will alert you about any changes by updating the "Last updated" date of these Legal Terms, and you waive any right to receive specific notice of each such change. It is your responsibility to periodically review these Legal Terms to stay informed of updates. You will be subject to, and will be deemed to have been made aware of and to have accepted, the changes in any revised Legal Terms by your continued use of the Services after the date such revised Legal Terms are posted.

    All users who are minors in the jurisdiction in which they reside (generally under the age of 18) must have the permission of, and be directly supervised by, their parent or guardian to use the Services. If you are a minor, you must have your parent or guardian read and agree to these Legal Terms prior to you using the Services.

    We recommend that you print a copy of these Legal Terms for your records.

    ## TABLE OF CONTENTS

    1. OUR SERVICES
    2. INTELLECTUAL PROPERTY RIGHTS
    3. USER REPRESENTATIONS
    4. USER REGISTRATION
    5. PURCHASES AND PAYMENT
    6. PROHIBITED ACTIVITIES
    7. USER GENERATED CONTRIBUTIONS
    8. CONTRIBUTION LICENCE
    9. MOBILE APPLICATION LICENCE
    10. SERVICES MANAGEMENT
    11. PRIVACY POLICY
    12. TERM AND TERMINATION
    13. MODIFICATIONS AND INTERRUPTIONS
    14. GOVERNING LAW
    15. DISPUTE RESOLUTION
    16. CORRECTIONS
    17. DISCLAIMER
    18. LIMITATIONS OF LIABILITY
    19. INDEMNIFICATION
    20. USER DATA
    21. ELECTRONIC COMMUNICATIONS, TRANSACTIONS, AND SIGNATURES
    22. MISCELLANEOUS
    23. CONTACT US

    ### 1. OUR SERVICES

    The information provided when using the Services is not intended for distribution to or use by any person or entity in any jurisdiction or country where such distribution or use would be contrary to law or regulation or which would subject us to any registration requirement within such jurisdiction or country. Accordingly, those persons who choose to access the Services from other locations do so on their own initiative and are solely responsible for compliance with local laws, if and to the extent local laws are applicable.

    ### 2. INTELLECTUAL PROPERTY RIGHTS

    Our intellectual property

    We are the owner or the licensee of all intellectual property rights in our Services, including all source code, databases, functionality, software, website designs, audio, video, text, photographs, and graphics in the Services (collectively, the "Content"), as well as the trademarks, service marks, and logos contained therein (the "Marks").

    Our Content and Marks are protected by copyright and trademark laws (and various other intellectual property rights and unfair competition laws) and treaties around the world.

    The Content and Marks are provided in or through the Services "AS IS" for your personal, non-commercial use only.

    Your use of our Services

    Subject to your compliance with these Legal Terms, including the "PROHIBITED ACTIVITIES" section below, we grant you a non-exclusive, non-transferable, revocable licence to:
    - access the Services; and
    - download or print a copy of any portion of the Content to which you have properly gained access,

    solely for your personal, non-commercial use.

    Except as set out in this section or elsewhere in our Legal Terms, no part of the Services and no Content or Marks may be copied, reproduced, aggregated, republished, uploaded, posted, publicly displayed, encoded, translated, transmitted, distributed, sold, licensed, or otherwise exploited for any commercial purpose whatsoever, without our express prior written permission.

    If you wish to make any use of the Services, Content, or Marks other than as set out in this section or elsewhere in our Legal Terms, please address your request to: contact@purplemaps.com. If we ever grant you the permission to post, reproduce, or publicly display any part of our Services or Content, you must identify us as the owners or licensors of the Services, Content, or Marks and ensure that any copyright or proprietary notice appears or is visible on posting, reproducing, or displaying our Content.

    We reserve all rights not expressly granted to you in and to the Services, Content, and Marks.

    Any breach of these Intellectual Property Rights will constitute a material breach of our Legal Terms and your right to use our Services will terminate immediately.

    Your submissions

    Please review this section and the "PROHIBITED ACTIVITIES" section carefully prior to using our Services to understand the (a) rights you give us and (b) obligations you have when you post or upload any content through the Services.

    - Submissions: By directly sending us any question, comment, suggestion, idea, feedback, or other information about the Services ("Submissions"), you agree to assign to us all intellectual property rights in such Submission. You agree that we shall own this Submission and be entitled to its unrestricted use and dissemination for any lawful purpose, commercial or otherwise, without acknowledgment or compensation to you.
    - You are responsible for what you post or upload: By sending us Submissions through any part of the Services you:
    1) confirm that you have read and agree with our "PROHIBITED ACTIVITIES" and will not post, send, publish, upload, or transmit through the Services any Submission that is illegal, harassing, hateful, harmful, defamatory, obscene, bullying, abusive, discriminatory, threatening to any person or group, sexually explicit, false, inaccurate, deceitful, or misleading;
    2) to the extent permissible by applicable law, waive any and all moral rights to any such Submission;
    3) warrant that any such Submission is original to you or that you have the necessary rights and licences to submit such Submissions and that you have full authority to grant us the above-mentioned rights in relation to your Submissions; and
    4) warrant and represent that your Submissions do not constitute confidential information.

    You are solely responsible for your Submissions and you expressly agree to reimburse us for any and all losses that we may suffer because of your breach of (a) this section, (b) any third party’s intellectual property rights, or (c) applicable law.

    ### 3. USER REPRESENTATIONS

    By using the Services, you represent and warrant that: (1) all registration information you submit will be true, accurate, current, and complete; (2) you will maintain the accuracy of such information and promptly update such registration information as necessary; (3) you have the legal capacity and you agree to comply with these Legal Terms; (4) you are not a minor in the jurisdiction in which you reside, or if a minor, you have received parental permission to use the Services; (5) you will not access the Services through automated or non-human means, whether through a bot, script or otherwise; (6) you will not use the Services for any illegal or unauthorised purpose; and (7) your use of the Services will not violate any applicable law or regulation.

    If you provide any information that is untrue, inaccurate, not current, or incomplete, we have the right to suspend or terminate your account and refuse any and all current or future use of the Services (or any portion thereof).

    ### 4. USER REGISTRATION

    You may be required to register to use the Services. You agree to keep your password confidential and will be responsible for all use of your account and password. We reserve the right to remove, reclaim, or change a username you select if we determine, in our sole discretion, that such username is inappropriate, obscene, or otherwise objectionable.

    ### 5. PURCHASES AND PAYMENT

    We accept the following forms of payment:

    You agree to provide current, complete, and accurate purchase and account information for all purchases made via the Services. You further agree to promptly update account and payment information, including email address, payment method, and payment card expiration date, so that we can complete your transactions and contact you as needed. Sales tax will be added to the price of purchases as deemed required by us. We may change prices at any time. All payments shall be in __________.

    You agree to pay all charges at the prices then in effect for your purchases and any applicable shipping fees, and you authorise us to charge your chosen payment provider for any such amounts upon placing your order. We reserve the right to correct any errors or mistakes in pricing, even if we have already requested or received payment.

    We reserve the right to refuse any order placed through the Services. We may, in our sole discretion, limit or cancel quantities purchased per person, per household, or per order. These restrictions may include orders placed by or under the same customer account, the same payment method, and/or orders that use the same billing or shipping address. We reserve the right to limit or prohibit orders that, in our sole judgement, appear to be placed by dealers, resellers, or distributors.

    ### 6. PROHIBITED ACTIVITIES

    You may not access or use the Services for any purpose other than that for which we make the Services available. The Services may not be used in connection with any commercial endeavours except those that are specifically endorsed or approved by us.

    As a user of the Services, you agree not to:
    - Systematically retrieve data or other content from the Services to create or compile, directly or indirectly, a collection, compilation, database, or directory without written permission from us.
    - Trick, defraud, or mislead us and other users, especially in any attempt to learn sensitive account information such as user passwords.
    - Circumvent, disable, or otherwise interfere with security-related features of the Services, including features that prevent or restrict the use or copying of any Content or enforce limitations on the use of the Services and/or the Content contained therein.
    - Disparage, tarnish, or otherwise harm, in our opinion, us and/or the Services.
    - Use any information obtained from the Services in order to harass, abuse, or harm another person.
    - Make improper use of our support services or submit false reports of abuse or misconduct.
    - Use the Services in a manner inconsistent with any applicable laws or regulations.
    - Engage in unauthorised framing of or linking to the Services.
    - Upload or transmit (or attempt to upload or to transmit) viruses, Trojan horses, or other material, including excessive use of capital letters and spamming (continuous posting of repetitive text), that interferes with any party’s uninterrupted use and enjoyment of the Services or modifies, impairs, disrupts, alters, or interferes with the use, features, functions, operation, or maintenance of the Services.
    - Engage in any automated use of the system, such as using scripts to send comments or messages, or using any data mining, robots, or similar data gathering and extraction tools.
    - Delete the copyright or other proprietary rights notice from any Content.
    - Attempt to impersonate another user or person or use the username of another user.
    - Upload or transmit (or attempt to upload or to transmit) any material that acts as a passive or active information collection or transmission mechanism, including without limitation, clear graphics interchange formats ("gifs"), 1×1 pixels, web bugs, cookies, or other similar devices (sometimes referred to as "spyware" or "passive collection mechanisms" or "pcms").
    - Interfere with, disrupt, or create an undue burden on the Services or the networks or services connected to the Services.
    - Harass, annoy, intimidate, or threaten any of our employees or agents engaged in providing any portion of the Services to you.
    - Attempt to bypass any measures of the Services designed to prevent or restrict access to the Services, or any portion of the Services.
    - Copy or adapt the Services' software, including but not limited to Flash, PHP, HTML, JavaScript, or other code.
    - Except as permitted by applicable law, decipher, decompile, disassemble, or reverse engineer any of the software comprising or in any way making up a part of the Services.
    - Except as may be the result of standard search engine or Internet browser usage, use, launch, develop, or distribute any automated system, including without limitation, any spider, robot, cheat utility, scraper, or offline reader that accesses the Services, or use or launch any unauthorised script or other software.
    - Use a buying agent or purchasing agent to make purchases on the Services.
    - Make any unauthorised use of the Services, including collecting usernames and/or email addresses of users by electronic or other means for the purpose of sending unsolicited email, or creating user accounts by automated means or under false pretences.
    - Use the Services as part of any effort to compete with us or otherwise use the Services and/or the Content for any revenue-generating endeavour or commercial enterprise.

    ### 7. USER GENERATED CONTRIBUTIONS

    The Services does not offer users to submit or post content. We may provide you with the opportunity to create, submit, post, display, transmit, perform, publish, distribute, or broadcast content and materials to us or on the Services, including but not limited to text, writings, video, audio, photographs, graphics, comments, suggestions, or personal information or other material (collectively, "Contributions"). Contributions may be viewable by other users of the Services and through third-party websites. As such, any Contributions you transmit may be treated in accordance with the Services' Privacy Policy. When you create or make available any Contributions, you thereby represent and warrant that:

    - The creation, distribution, transmission, public display, or performance, and the accessing, downloading, or copying of your Contributions do not and will not infringe the proprietary rights, including but not limited to the copyright, patent, trademark, trade secret, or moral rights of any third party.
    - You are the creator and owner of or have the necessary licences, rights, consents, releases, and permissions to use and to authorise us, the Services, and other users of the Services to use your Contributions in any manner contemplated by the Services and these Legal Terms.
    - You have the written consent, release, and/or permission of each and every identifiable individual person in your Contributions to use the name or likeness of each and every such identifiable individual person to enable inclusion and use of your Contributions in any manner contemplated by the Services and these Legal Terms.
    - Your Contributions are not false, inaccurate, or misleading.
    - Your Contributions are not unsolicited or unauthorised advertising, promotional materials, pyramid schemes, chain letters, spam, mass mailings, or other forms of solicitation.
    - Your Contributions are not obscene, lewd, lascivious, filthy, violent, harassing, libellous, slanderous, or otherwise objectionable (as determined by us).
    - Your Contributions do not ridicule, mock, disparage, intimidate, or abuse anyone.
    - Your Contributions are not used to harass or threaten (in the legal sense of those terms) any other person and to promote violence against a specific person or class of people.
    - Your Contributions do not violate any applicable law, regulation, or rule.
    - Your Contributions do not violate the privacy or publicity rights of any third party.
    - Your Contributions do not violate any applicable law concerning child pornography, or otherwise intended to protect the health or well-being of minors.
    - Your Contributions do not include any offensive comments that are connected to race, national origin, gender, sexual preference, or physical handicap.
    - Your Contributions do not otherwise violate, or link to material that violates, any provision of these Legal Terms, or any applicable law or regulation.

    Any use of the Services in violation of the foregoing violates these Legal Terms and may result in, among other things, termination or suspension of your rights to use the Services.

    ### 8. CONTRIBUTION LICENCE

    You and Services agree that we may access, store, process, and use any information and personal data that you provide following the terms of the Privacy Policy and your choices (including settings).

    By submitting suggestions or other feedback regarding the Services, you agree that we can use and share such feedback for any purpose without compensation to you.

    We do not assert any ownership over your Contributions. You retain full ownership of all of your Contributions and any intellectual property rights or other proprietary rights associated with your Contributions. We are not liable for any statements or representations in your Contributions provided by you in any area on the Services. You are solely responsible for your Contributions to the Services and you expressly agree to exonerate us from any and all responsibility and to refrain from any legal action against us regarding your Contributions.

    ### 9. MOBILE APPLICATION LICENCE

    Use Licence

    If you access the Services via the App, then we grant you a revocable, non-exclusive, non-transferable, limited right to install and use the App on wireless electronic devices owned or controlled by you, and to access and use the App on such devices strictly in accordance with the terms and conditions of this mobile application licence contained in these Legal Terms. You shall not: (1) except as permitted by applicable law, decompile, reverse engineer, disassemble, attempt to derive the source code of, or decrypt the App; (2) make any modification, adaptation, improvement, enhancement, translation, or derivative work from the App; (3) violate any applicable laws, rules, or regulations in connection with your access or use of the App; (4) remove, alter, or obscure any proprietary notice (including any notice of copyright or trademark) posted by us or the licensors of the App; (5) use the App for any revenue-generating endeavour, commercial enterprise, or other purpose for which it is not designed or intended; (6) make the App available over a network or other environment permitting access or use by multiple devices or users at the same time; (7) use the App for creating a product, service, or software that is, directly or indirectly, competitive with or in any way a substitute for the App; (8) use the App to send automated queries to any website or to send any unsolicited commercial email; or (9) use any proprietary information or any of our interfaces or our other intellectual property in the design, development, manufacture, licensing, or distribution of any applications, accessories, or devices for use with the App.

    ### Apple and Android Devices

    The following terms apply when you use the App obtained from either the Apple Store or Google Play (each an "App Distributor") to access the Services: (1) the licence granted to you for our App is limited to a non-transferable licence to use the application on a device that utilises the Apple iOS or Android operating systems, as applicable, and in accordance with the usage rules set forth in the applicable App Distributor’s terms of service; (2) we are responsible for providing any maintenance and support services with respect to the App as specified in the terms and conditions of this mobile application licence contained in these Legal Terms or as otherwise required under applicable law, and you acknowledge that each App Distributor has no obligation whatsoever to furnish any maintenance and support services with respect to the App; (3) in the event of any failure of the App to conform to any applicable warranty, you may notify the applicable App Distributor, and the App Distributor, in accordance with its terms and policies, may refund the purchase price, if any, paid for the App, and to the maximum extent permitted by applicable law, the App Distributor will have no other warranty obligation whatsoever with respect to the App; (4) you represent and warrant that (i) you are not located in a country that is subject to a US government embargo, or that has been designated by the US government as a "terrorist supporting" country and (ii) you are not listed on any US government list of prohibited or restricted parties; (5) you must comply with applicable third-party terms of agreement when using the App, e.g. if you have a VoIP application, then you must not be in violation of their wireless data service agreement when using the App; and (6) you acknowledge and agree that the App Distributors are third-party beneficiaries of the terms and conditions in this mobile application licence contained in these Legal Terms, and that each App Distributor will have the right (and will be deemed to have accepted the right) to enforce the terms and conditions in this mobile application licence contained in these Legal Terms against you as a third-party beneficiary thereof.

    ### 10. SERVICES MANAGEMENT

    We reserve the right, but not the obligation, to: (1) monitor the Services for violations of these Legal Terms; (2) take appropriate legal action against anyone who, in our sole discretion, violates the law or these Legal Terms, including without limitation, reporting such user to law enforcement authorities; (3) in our sole discretion and without limitation, refuse, restrict access to, limit the availability of, or disable (to the extent technologically feasible) any of your Contributions or any portion thereof; (4) in our sole discretion and without limitation, notice, or liability, to remove from the Services or otherwise disable all files and content that are excessive in size or are in any way burdensome to our systems; and (5) otherwise manage the Services in a manner designed to protect our rights and property and to facilitate the proper functioning of the Services.

    ### 11. PRIVACY POLICY

    We care about data privacy and security. Please review our Privacy Policy: https://odiseiapurplemaps.streamlit.app/politica-de-privacidad. By using the Services, you agree to be bound by our Privacy Policy, which is incorporated into these Legal Terms. Please be advised the Services are hosted in Spain. If you access the Services from any other region of the world with laws or other requirements governing personal data collection, use, or disclosure that differ from applicable laws in Spain, then through your continued use of the Services, you are transferring your data to Spain, and you expressly consent to have your data transferred to and processed in Spain.

    ### 12. TERM AND TERMINATION

    These Legal Terms shall remain in full force and effect while you use the Services. WITHOUT LIMITING ANY OTHER PROVISION OF THESE LEGAL TERMS, WE RESERVE THE RIGHT TO, IN OUR SOLE DISCRETION AND WITHOUT NOTICE OR LIABILITY, DENY ACCESS TO AND USE OF THE SERVICES (INCLUDING BLOCKING CERTAIN IP ADDRESSES), TO ANY PERSON FOR ANY REASON OR FOR NO REASON, INCLUDING WITHOUT LIMITATION FOR BREACH OF ANY REPRESENTATION, WARRANTY, OR COVENANT CONTAINED IN THESE LEGAL TERMS OR OF ANY APPLICABLE LAW OR REGULATION. WE MAY TERMINATE YOUR USE OR PARTICIPATION IN THE SERVICES OR DELETE YOUR ACCOUNT AND ANY CONTENT OR INFORMATION THAT YOU POSTED AT ANY TIME, WITHOUT WARNING, IN OUR SOLE DISCRETION.

    If we terminate or suspend your account for any reason, you are prohibited from registering and creating a new account under your name, a fake or borrowed name, or the name of any third party, even if you may be acting on behalf of the third party. In addition to terminating or suspending your account, we reserve the right to take appropriate legal action, including without limitation pursuing civil, criminal, and injunctive redress.

    ### 13. MODIFICATIONS AND INTERRUPTIONS

    We reserve the right to change, modify, or remove the contents of the Services at any time or for any reason at our sole discretion without notice. However, we have no obligation to update any information on our Services. We will not be liable to you or any third party for any modification, price change, suspension, or discontinuance of the Services.

    We cannot guarantee the Services will be available at all times. We may experience hardware, software, or other problems or need to perform maintenance related to the Services, resulting in interruptions, delays, or errors. We reserve the right to change, revise, update, suspend, discontinue, or otherwise modify the Services at any time or for any reason without notice to you. You agree that we have no liability whatsoever for any loss, damage, or inconvenience caused by your inability to access or use the Services during any downtime or discontinuance of the Services. Nothing in these Legal Terms will be construed to obligate us to maintain and support the Services or to supply any corrections, updates, or releases in connection therewith.

    ### 14. GOVERNING LAW

    These Legal Terms are governed by and interpreted following the laws of Spain, and the use of the United Nations Convention of Contracts for the International Sales of Goods is expressly excluded. If your habitual residence is in the EU, and you are a consumer, you additionally possess the protection provided to you by obligatory provisions of the law in your country to residence. Purple Maps and yourself both agree to submit to the non-exclusive jurisdiction of the courts of __________, which means that you may make a claim to defend your consumer protection rights in regards to these Legal Terms in Spain, or in the EU country in which you reside.

    ### 15. DISPUTE RESOLUTION

    Informal Negotiations

    To expedite resolution and control the cost of any dispute, controversy, or claim related to these Legal Terms (each a "Dispute" and collectively, the "Disputes") brought by either you or us (individually, a "Party" and collectively, the "Parties"), the Parties agree to first attempt to negotiate any Dispute (except those Disputes expressly provided below) informally for at least thirty (30) days before initiating arbitration. Such informal negotiations commence upon written notice from one Party to the other Party.

    #### Binding Arbitration

    Any dispute arising from the relationships between the Parties to these Legal Terms shall be determined by one arbitrator who will be chosen in accordance with the Arbitration and Internal Rules of the European Court of Arbitration being part of the European Centre of Arbitration having its seat in Strasbourg, and which are in force at the time the application for arbitration is filed, and of which adoption of this clause constitutes acceptance. The seat of arbitration shall be Madrid, Spain. The language of the proceedings shall be Spanish. Applicable rules of substantive law shall be the law of Spain.

    #### Restrictions

    The Parties agree that any arbitration shall be limited to the Dispute between the Parties individually. To the full extent permitted by law, (a) no arbitration shall be joined with any other proceeding; (b) there is no right or authority for any Dispute to be arbitrated on a class-action basis or to utilise class action procedures; and (c) there is no right or authority for any Dispute to be brought in a purported representative capacity on behalf of the general public or any other persons.

    Exceptions to Informal Negotiations and Arbitration

    The Parties agree that the following Disputes are not subject to the above provisions concerning informal negotiations binding arbitration: (a) any Disputes seeking to enforce or protect, or concerning the validity of, any of the intellectual property rights of a Party; (b) any Dispute related to, or arising from, allegations of theft, piracy, invasion of privacy, or unauthorised use; and (c) any claim for injunctive relief. If this provision is found to be illegal or unenforceable, then neither Party will elect to arbitrate any Dispute falling within that portion of this provision found to be illegal or unenforceable and such Dispute shall be decided by a court of competent jurisdiction within the courts listed for jurisdiction above, and the Parties agree to submit to the personal jurisdiction of that court.

    ### 16. CORRECTIONS

    There may be information on the Services that contains typographical errors, inaccuracies, or omissions, including descriptions, pricing, availability, and various other information. We reserve the right to correct any errors, inaccuracies, or omissions and to change or update the information on the Services at any time, without prior notice.

    ### 17. DISCLAIMER

    THE SERVICES ARE PROVIDED ON AN AS-IS AND AS-AVAILABLE BASIS. YOU AGREE THAT YOUR USE OF THE SERVICES WILL BE AT YOUR SOLE RISK. TO THE FULLEST EXTENT PERMITTED BY LAW, WE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, IN CONNECTION WITH THE SERVICES AND YOUR USE THEREOF, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. WE MAKE NO WARRANTIES OR REPRESENTATIONS ABOUT THE ACCURACY OR COMPLETENESS OF THE SERVICES' CONTENT OR THE CONTENT OF ANY WEBSITES OR MOBILE APPLICATIONS LINKED TO THE SERVICES AND WE WILL ASSUME NO LIABILITY OR RESPONSIBILITY FOR ANY (1) ERRORS, MISTAKES, OR INACCURACIES OF CONTENT AND MATERIALS, (2) PERSONAL INJURY OR PROPERTY DAMAGE, OF ANY NATURE WHATSOEVER, RESULTING FROM YOUR ACCESS TO AND USE OF THE SERVICES, (3) ANY UNAUTHORISED ACCESS TO OR USE OF OUR SECURE SERVERS AND/OR ANY AND ALL PERSONAL INFORMATION AND/OR FINANCIAL INFORMATION STORED THEREIN, (4) ANY INTERRUPTION OR CESSATION OF TRANSMISSION TO OR FROM THE SERVICES, (5) ANY BUGS, VIRUSES, TROJAN HORSES, OR THE LIKE WHICH MAY BE TRANSMITTED TO OR THROUGH THE SERVICES BY ANY THIRD PARTY, AND/OR (6) ANY ERRORS OR OMISSIONS IN ANY CONTENT AND MATERIALS OR FOR ANY LOSS OR DAMAGE OF ANY KIND INCURRED AS A RESULT OF THE USE OF ANY CONTENT POSTED, TRANSMITTED, OR OTHERWISE MADE AVAILABLE VIA THE SERVICES. WE DO NOT WARRANT, ENDORSE, GUARANTEE, OR ASSUME RESPONSIBILITY FOR ANY PRODUCT OR SERVICE ADVERTISED OR OFFERED BY A THIRD PARTY THROUGH THE SERVICES, ANY HYPERLINKED WEBSITE, OR ANY WEBSITE OR MOBILE APPLICATION FEATURED IN ANY BANNER OR OTHER ADVERTISING, AND WE WILL NOT BE A PARTY TO OR IN ANY WAY BE RESPONSIBLE FOR MONITORING ANY TRANSACTION BETWEEN YOU AND ANY THIRD-PARTY PROVIDERS OF PRODUCTS OR SERVICES. AS WITH THE PURCHASE OF A PRODUCT OR SERVICE THROUGH ANY MEDIUM OR IN ANY ENVIRONMENT, YOU SHOULD USE YOUR BEST JUDGEMENT AND EXERCISE CAUTION WHERE APPROPRIATE.

    ### 18. LIMITATIONS OF LIABILITY

    IN NO EVENT WILL WE OR OUR DIRECTORS, EMPLOYEES, OR AGENTS BE LIABLE TO YOU OR ANY THIRD PARTY FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL, EXEMPLARY, INCIDENTAL, SPECIAL, OR PUNITIVE DAMAGES, INCLUDING LOST PROFIT, LOST REVENUE, LOSS OF DATA, OR OTHER DAMAGES ARISING FROM YOUR USE OF THE SERVICES, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. NOTWITHSTANDING ANYTHING TO THE CONTRARY CONTAINED HEREIN, OUR LIABILITY TO YOU FOR ANY CAUSE WHATSOEVER AND REGARDLESS OF THE FORM OF THE ACTION, WILL AT ALL TIMES BE LIMITED TO THE LESSER OF THE AMOUNT PAID, IF ANY, BY YOU TO US OR ____. CERTAIN US STATE LAWS AND INTERNATIONAL LAWS DO NOT ALLOW LIMITATIONS ON IMPLIED WARRANTIES OR THE EXCLUSION OR LIMITATION OF CERTAIN DAMAGES. IF THESE LAWS APPLY TO YOU, SOME OR ALL OF THE ABOVE DISCLAIMERS OR LIMITATIONS MAY NOT APPLY TO YOU, AND YOU MAY HAVE ADDITIONAL RIGHTS.

    ### 19. INDEMNIFICATION

    You agree to defend, indemnify, and hold us harmless, including our subsidiaries, affiliates, and all of our respective officers, agents, partners, and employees, from and against any loss, damage, liability, claim, or demand, including reasonable attorneys’ fees and expenses, made by any third party due to or arising out of: (1) use of the Services; (2) breach of these Legal Terms; (3) any breach of your representations and warranties set forth in these Legal Terms; (4) your violation of the rights of a third party, including but not limited to intellectual property rights; or (5) any overt harmful act toward any other user of the Services with whom you connected via the Services. Notwithstanding the foregoing, we reserve the right, at your expense, to assume the exclusive defence and control of any matter for which you are required to indemnify us, and you agree to cooperate, at your expense, with our defence of such claims. We will use reasonable efforts to notify you of any such claim, action, or proceeding which is subject to this indemnification upon becoming aware of it.

    ### 20. USER DATA

    We will maintain certain data that you transmit to the Services for the purpose of managing the performance of the Services, as well as data relating to your use of the Services. Although we perform regular routine backups of data, you are solely responsible for all data that you transmit or that relates to any activity you have undertaken using the Services. You agree that we shall have no liability to you for any loss or corruption of any such data, and you hereby waive any right of action against us arising from any such loss or corruption of such data.

    ### 21. ELECTRONIC COMMUNICATIONS, TRANSACTIONS, AND SIGNATURES

    Visiting the Services, sending us emails, and completing online forms constitute electronic communications. You consent to receive electronic communications, and you agree that all agreements, notices, disclosures, and other communications we provide to you electronically, via email and on the Services, satisfy any legal requirement that such communication be in writing. YOU HEREBY AGREE TO THE USE OF ELECTRONIC SIGNATURES, CONTRACTS, ORDERS, AND OTHER RECORDS, AND TO ELECTRONIC DELIVERY OF NOTICES, POLICIES, AND RECORDS OF TRANSACTIONS INITIATED OR COMPLETED BY US OR VIA THE SERVICES. You hereby waive any and all defences you may have based on the electronic form of these Legal Terms and the lack of signing by the parties hereto to execute these Legal Terms.

    ### 22. MISCELLANEOUS

    These Legal Terms and any policies or operating rules posted by us on the Services or in respect to the Services constitute the entire agreement and understanding between you and us. Our failure to exercise or enforce any right or provision of these Legal Terms shall not operate as a waiver of such right or provision. These Legal Terms operate to the fullest extent permissible by law. We may assign any or all of our rights and obligations to others at any time. We shall not be responsible or liable for any loss, damage, delay, or failure to act caused by any cause beyond our reasonable control. If any provision or part of a provision of these Legal Terms is determined to be unlawful, void, or unenforceable, that provision or part of the provision is deemed severable from these Legal Terms and does not affect the validity and enforceability of any remaining provisions. There is no joint venture, partnership, employment or agency relationship created between you and us as a result of these Legal Terms or use of the Services. You agree that these Legal Terms will not be construed against us by virtue of having drafted them. You hereby waive any and all defences you may have based on the electronic form of these Legal Terms and the lack of signing by the parties hereto to execute these Legal Terms.

    ### 23. CONTACT US

    In order to resolve a complaint regarding the Services or to receive further information regarding use of the Services, please contact us at:

    Purple Maps
    Calle Mayor, 10
    Madrid, Madrid 28013
    Spain
    Phone: +34 900 123 456
    contact@purplemaps.com


    # PRIVACY POLICY

    **Last updated:** February 26, 2025

    This Privacy Notice for Purple Maps ("we", "us", or "our") describes how and why we might access, collect, store, use, and/or share ("process") your personal information when you use our services ("Services"), including when you:

    - Visit our website at [https://odiseiapurplemaps.streamlit.app](https://odiseiapurplemaps.streamlit.app) or any website of ours that links to this Privacy Notice.
    - Download and use our mobile application (Purple Maps) or any other application of ours that links to this Privacy Notice.
    - Engage with us in other related ways, including any sales, marketing, or events.

    If you have any questions or concerns, reading this Privacy Notice will help you understand your privacy rights and choices. We are responsible for making decisions about how your personal information is processed. If you do not agree with our policies and practices, please do not use our Services. For further questions or concerns, please contact us at [contact@purplemaps.com](mailto:contact@purplemaps.com).

    ---

    ## SUMMARY OF KEY POINTS

    This summary provides key points from our Privacy Notice. You can find more details by clicking the link following each key point or by using the table of contents below to find the section you are looking for.

    - **What personal information do we process?**  
    We may process personal information depending on how you interact with our Services, the choices you make, and the products and features you use.  
    *Learn more about the personal information you disclose to us.*

    - **Do we process any sensitive personal information?**  
    Some information (e.g., racial or ethnic origins, sexual orientation, religious beliefs) may be considered sensitive in certain jurisdictions. We do not process sensitive personal information.

    - **Do we collect any information from third parties?**  
    We do not collect information from third parties.

    - **How do we process your information?**  
    We process your information to provide, improve, and administer our Services, communicate with you, ensure security and fraud prevention, and comply with the law. We may also process your information for other purposes with your consent.

    - **When and with whom do we share your personal information?**  
    We may share your information in specific situations and with specific third parties.  
    *Learn more about when and with whom we share your personal information.*

    - **How do we keep your information safe?**  
    We have appropriate organizational and technical measures to protect your information, although no method is 100% secure.  
    *Learn more about how we keep your information safe.*

    - **What are your rights?**  
    Depending on your location, you may have certain rights regarding your personal information.  
    *Learn more about your privacy rights.*

    - **How do you exercise your rights?**  
    The easiest way to exercise your rights is by submitting a data subject access request or contacting us. We will consider and act upon any request in accordance with applicable data protection laws.

    For more details on how we handle your information, please review the full Privacy Notice below.

    ---

    ## TABLE OF CONTENTS

    1. [What Information Do We Collect?](#1-what-information-do-we-collect)
    2. [How Do We Process Your Information?](#2-how-do-we-process-your-information)
    3. [What Legal Bases Do We Rely On to Process Your Personal Information?](#3-what-legal-bases-do-we-rely-on-to-process-your-personal-information)
    4. [When and With Whom Do We Share Your Personal Information?](#4-when-and-with-whom-do-we-share-your-personal-information)
    5. [Do We Offer Artificial Intelligence-Based Products?](#5-do-we-offer-artificial-intelligence-based-products)
    6. [How Long Do We Keep Your Information?](#6-how-long-do-we-keep-your-information)
    7. [How Do We Keep Your Information Safe?](#7-how-do-we-keep-your-information-safe)
    8. [Do We Collect Information from Minors?](#8-do-we-collect-information-from-minors)
    9. [What Are Your Privacy Rights?](#9-what-are-your-privacy-rights)
    10. [Controls for Do-Not-Track Features](#10-controls-for-do-not-track-features)
    11. [Do We Make Updates to This Notice?](#11-do-we-make-updates-to-this-notice)
    12. [How Can You Contact Us About This Notice?](#12-how-can-you-contact-us-about-this-notice)
    13. [How Can You Review, Update, or Delete the Data We Collect from You?](#13-how-can-you-review-update-or-delete-the-data-we-collect-from-you)

    ---

    ## 1. What Information Do We Collect?

    ### Personal Information You Disclose to Us

    **In Short:** We collect personal information that you provide to us.

    We collect personal information that you voluntarily provide to us when you:
    - Register on the Services.
    - Express an interest in obtaining information about us or our products and Services.
    - Participate in activities on the Services.
    - Contact us.

    **Personal Information Provided by You:**  
    The information we collect depends on the context of your interactions with us and the Services, the choices you make, and the products and features you use. This may include:
    - Names
    - Phone numbers
    - Email addresses

    **Sensitive Information:**  
    We do not process sensitive information.

    **Application Data:**  
    If you use our application(s), we may collect additional information if you grant access or permission, such as:
    - **Geolocation Information:**  
    We may request access to track location-based information from your mobile device—either continuously or while using our mobile app—to provide certain location-based services. You can change these permissions in your device’s settings.

    All personal information you provide must be true, complete, and accurate. Please notify us of any changes to your personal information.

    ---

    ## 2. How Do We Process Your Information?

    **In Short:** We process your information to provide, improve, and administer our Services, communicate with you, ensure security and fraud prevention, and comply with law. We may also process your information for other purposes with your consent.

    We process your personal information for various reasons, including:
    - **Facilitating Account Creation and Authentication:**  
    To enable you to create and log in to your account and to maintain its proper functioning.
    - **Saving or Protecting an Individual’s Vital Interest:**  
    To prevent harm by processing your information when necessary.
    - **Secure Chat Data Retention for Potential Legal Use:**  
    We offer users the option to store their chat conversation logs with explicit consent, secured by high-level governmental credentials (e.g., electronic ID/digital certificate). This feature allows you to preserve conversation records that may serve as legal evidence. You can request deletion of these stored logs at any time, ensuring full control over your data.

    ---

    ## 3. What Legal Bases Do We Rely On to Process Your Personal Information?

    **In Short:** We only process your personal information when we have a valid legal reason to do so under applicable law. These include:
    - **Consent:**  
    We may process your information if you have given us permission to use your personal information for a specific purpose. You may withdraw your consent at any time.
    - **Legitimate Interests:**  
    We may process your information when it is necessary for our legitimate business interests, provided these interests do not override your rights and freedoms. For instance, to:
    - Provide a secure mechanism for retaining conversation logs as legal evidence.
    - Ensure data authenticity and confidentiality via government-level security credentials.
    - Allow the deletion of logs upon request.
    - **Legal Obligations:**  
    We process your information as required to comply with legal obligations, such as cooperating with law enforcement or regulatory agencies, defending our legal rights, or participating in litigation.
    - **Vital Interests:**  
    We may process your information to protect your vital interests or those of a third party, particularly in situations involving potential threats to safety.

    ---

    ## 4. When and With Whom Do We Share Your Personal Information?

    **In Short:** We may share your personal information in specific situations and with certain third parties.

    ### Business Transfers
    We may share or transfer your information in connection with, or during negotiations for, any merger, sale of company assets, financing, or acquisition of all or part of our business to another company.

    ---

    ## 5. Do We Offer Artificial Intelligence-Based Products?

    **In Short:** Yes, we offer products, features, or tools powered by artificial intelligence, machine learning, or similar technologies (collectively, "AI Products").

    Our AI Products are designed to:
    - Enhance your experience.
    - Provide innovative solutions.

    ### Our AI Products Include:
    - AI bots
    - AI predictive analytics

    ### How We Process Your Data Using AI
    All personal information processed using our AI Products is handled in accordance with this Privacy Notice and our agreements with third parties, ensuring high security and safeguarding your personal information.

    ---

    ## 6. How Long Do We Keep Your Information?

    **In Short:** We retain your personal information only as long as necessary to fulfill the purposes outlined in this Privacy Notice, unless a longer retention period is required by law.

    Once there is no ongoing legitimate business need for your personal information, we will either delete or anonymize it. If deletion is not possible (e.g., due to backup archives), we will securely store and isolate your personal information until it can be deleted.

    ---

    ## 7. How Do We Keep Your Information Safe?

    **In Short:** We implement organizational and technical security measures to protect your personal information.

    While we strive to secure your data, no method of transmission over the Internet or electronic storage is 100% secure. Therefore, we cannot guarantee absolute security against hackers, cybercriminals, or other unauthorized third parties. Access the Services within a secure environment to minimize risk.

    ---

    ## 8. Do We Collect Information from Minors?

    **In Short:** We do not knowingly collect data from or market to children under 18 years of age.

    We do not knowingly collect, solicit, or market personal information from children under 18. By using our Services, you confirm that you are at least 18 years old or that you are the parent or guardian of a minor who has consented to the minor's use of the Services. If we discover that personal information from users under 18 has been collected, we will deactivate the account and take steps to promptly delete the data.

    ---

    ## 9. What Are Your Privacy Rights?

    **In Short:** Depending on your location (e.g., EEA, UK, Switzerland), you have rights that allow you greater access to and control over your personal information.

    These rights may include:
    - Requesting access to and obtaining a copy of your personal information.
    - Requesting rectification or erasure of your data.
    - Restricting the processing of your personal information.
    - Data portability (if applicable).
    - Not being subject to automated decision-making.

    You may exercise these rights by contacting us as detailed in the [How Can You Contact Us About This Notice?](#12-how-can-you-contact-us-about-this-notice) section.

    If you believe we are unlawfully processing your personal information (and you are in the EEA or UK), you have the right to lodge a complaint with your local data protection authority. In Switzerland, please contact the Federal Data Protection and Information Commissioner.

    **Withdrawing your consent:**  
    If we process your information based on your consent, you can withdraw it at any time. Note that withdrawing consent does not affect the lawfulness of prior processing.

    **Account Information:**  
    If you wish to review or update your account information, or terminate your account, please contact us. We may retain certain data to prevent fraud, assist with investigations, enforce our legal terms, or comply with legal requirements.

    For questions regarding your privacy rights, email us at [contact@purplemaps.com](mailto:contact@purplemaps.com).

    ---

    ## 10. Controls for Do-Not-Track Features

    Most web browsers and some mobile operating systems and applications include a Do-Not-Track ("DNT") feature. Currently, no uniform standard for recognizing and implementing DNT signals exists. Therefore, we do not respond to DNT signals or similar mechanisms. Should a standard be adopted in the future, we will update our practices accordingly.

    ---

    ## 11. Do We Make Updates to This Notice?

    **In Short:** Yes, we will update this notice as necessary to remain compliant with relevant laws.

    We may update this Privacy Notice periodically. The updated version will be indicated by a revised date at the top of this document. If material changes are made, we may notify you through a prominent notice or direct communication. We encourage you to review this Privacy Notice regularly.

    ---

    ## 12. How Can You Contact Us About This Notice?

    If you have any questions or comments about this Privacy Notice, please contact us by mail at:

    **Purple Maps**  
    Calle Mayor, 10  
    Madrid, Madrid 28013  
    Spain

    ---

    ## 13. How Can You Review, Update, or Delete the Data We Collect from You?

    Based on the laws applicable in your country, you may have the right to:
    - Request access to the personal information we collect.
    - Obtain details about how we have processed your information.
    - Request correction of any inaccuracies.
    - Request deletion of your personal information.
    - Withdraw your consent for processing.

    To review, update, or delete your personal information, please submit a data subject access request.

    ---

    _Política de privacidad | Condiciones de uso | Descargo de responsabilidad | Política de cookies | Soporte | Limitar el uso de mi información_  
    _No vender ni compartir mis datos personales | Preferencias de consentimiento_


    """,
    unsafe_allow_html=False
)

st.markdown('</div>', unsafe_allow_html=True)

with st.sidebar:

        st.markdown(
            """
            <style>
                /* Cambiar el fondo del sidebar a morado claro */
                [data-testid="stSidebar"] {
                    background-color: #c39bd8 !important;
                }
                
                /* Cambiar el color del texto en el sidebar a blanco */
                [data-testid="stSidebar"] * {
                    color: white !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )


        usuario = st.session_state.get("usuario", None)
        permisos = st.session_state.get("permisos", "Usuaria")  # Valor por defecto si no existe


        dfusuarios = pd.read_csv('usuarios.csv')

        # Filtrar usuario
        dfUsuario = dfusuarios[dfusuarios['usuario'] == usuario]

        # ✅ Verificar si dfUsuario no está vacío antes de acceder a valores
        if not dfUsuario.empty:
            nombre = dfUsuario.iloc[0]["nombre"]  # Acceder a la primera fila de forma segura
            permisos = dfUsuario.iloc[0]["permisos"]
        else:
            nombre = "Invitada"
            permisos = "Usuaria"

        # usuario = st.session_state["usuario"]
        # permisos = st.session_state["permisos"]

        st.image("img/Purple_Maps.png", width=100)
        # Cargamos la tabla de usuarios
        dfusuarios = pd.read_csv('usuarios.csv')
        # Filtramos la tabla de usuarios
        dfUsuario =dfusuarios[(dfusuarios['usuario']==usuario)]
        # Cargamos el nombre del usuario
        nombre= dfUsuario['nombre'].values[0]
        permisos= dfUsuario['permisos'].values[0]
        #Mostramos el nombre del usuario
        st.write(f"Hola **:blue-background[{nombre}]** ")
        # Mostramos los enlaces de páginas
        st.subheader("Funcionalidades")
        st.page_link("inicio.py", label="Inicio", icon=":material/home:")
        st.page_link("pages/mapa_violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
        st.page_link("pages/chat_violeta.py", label="Chat Violeta", icon=":material/chat:")
        st.page_link("pages/alertas_violeta.py", label="Alertas ", icon=":material/report:")
        st.page_link("pages/politica_privacidad_terminos_de_uso.py", label="Documentación", icon=":material/contact_support:")
        st.page_link("pages/forms_peticiones.py", label="Solicitud de PV", icon=":material/contact_page:")
        if permisos == "administradora":
            st.subheader("Gestión y administración")
            st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")
            st.page_link("pages/modelo_optimizacion_estatal.py", label="Modelo Optimización Estatal", icon=":material/modeling:")
            st.page_link("pages/modelo_optimizacion_local.py", label="Modelo Optimización Local", icon=":material/modeling:")

        st.session_state["usuario"] = usuario
        st.session_state["permisos"] = permisos  # Guardar permisos globalmen

        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()