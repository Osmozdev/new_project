import streamlit as st
from PIL import Image
import base64


def _get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = _get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


def azure_course():
    st.markdown("""
    
    <img src="https://mbamci.com/wp-content/uploads/2015/03/microsoft-azure1.png" alt="Azure image" style="height: 10%; width: 100%;">
    
    """, unsafe_allow_html=True)
    st.title('Azure Fundamentals Course (AZ-900)')

    st.subheader('What is cloud computing ?')

    st.markdown('It is a network of remote servers used to : ')
    st.markdown('* Store Data')
    st.markdown('* Manage Data')
    st.markdown('* Process Data')
    st.markdown(
        'Before the Cloud Boom, the servers/computers/IT peoples **were on the company premise**')
    st.markdown("Then, right now and thanks to the cloud, company and particular users don't need anymore to :")
    st.markdown('* Pay the real estates')
    st.markdown('* Hire IT peoples')
    st.markdown('* Pay the servers')
    st.markdown('* Hold issues risks (Such as what happened at [OVH]('
                'https://www.datacenterknowledge.com/uptime/fire-has-destroyed-ovh-s-strasbourg-data-center-sbg2)). ')
    st.markdown('* Pay for the maintenance')
    st.markdown(
        'Just because the Cloud Providers (Such as [Amazon]('
        'https://www.google.com/aclk?sa=L&ai=DChcSEwiPjMXXvs_0AhUHh9UKHUqbAewYABABGgJ3cw&ae=2&sig=AOD64_3'
        '-YY_Q2X9K3cbLLL6CltWAcxgOpQ&q&adurl&ved=2ahUKEwi0_7vXvs_0AhVtx4UKHcvhDVcQ0Qx6BAgDEAE), [Microsoft]('
        'https://azure.microsoft.com/fr-fr/) or [Google](https://cloud.google.com/)) '
        'hold and maintain all the points below.')

    st.subheader('Common Cloud Services')
    st.markdown(' You can find hundred of cloud services, such as :')
    st.markdown('**Computing services** : Virtual computer that can run applications, programs and code.')
    st.markdown('**Storages services** : Virtual hard drive to store structured or unstructured files.')
    st.markdown('**Networking services** : Virtual network that enable connexion between the different services')
    st.markdown('**Databases services** : Virtual database for storing data')

    st.subheader('What is Azure ?')
    st.markdown(
        'Azure is a **cloud computing platform** that enable to use multiple cloud services. It is a product widely used and has been develloped by Microsoft.')
    st.markdown('Fun Fact : Azure means "bright blue color of the cloudless sky" :cloud:')

    st.subheader('What are the benefits of Cloud Computing ?')
    st.markdown('1) **Cost-effective** : you pay for what you consume.')
    st.markdown('2) **Global** : you can work from anywhere in the world.')
    st.markdown(
        '3) **Secure** : Cloud takes care of physical security. Moreover, the user has the ability to configure access to granular level')
    st.markdown('4) **Reliable** : You have data backup, disaster recovery, data replication etc.')
    st.markdown('5) **Scalable** : You can increase or decrease resources and services based on demand')
    st.markdown('6) **Elastic** : Automate scaling during spikes and drop in demand')
    st.markdown('7) **Current** : The hardware are constantly upgraded without interruption for you.')

    st.subheader('Types of cloud computing')
    st.markdown(
        '* **SaaS Software as a Service** : A product that is run and managed by the service provider (ex: Salesforce, Office365, Gmail ...)')
    st.markdown(
        '* **PaaS Plateform as a Service** : Focus on the deployement and management of your apps. (ex : Heroku, Google app engine)')
    st.markdown(
        '* **Infrastructure as a Service** : Basic building blocs for cloud IT, provide access to network features, computers and storage space. (ex: Microsoft Azure, Oracle Cloud, AWS)')

    st.subheader('Types of Cloud Computing Responsabilities')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("![Service responsabilities](https://www.britlog.com/files/responsabilites-onpremise-cloud.png)")
    with col2:
        st.markdown("According to the table on the left, you understand that :")
        st.markdown("* When a company holds everything **on-premise**, it has to **personnaly** take everything in "
                    "charge, it can be really expensive.")
        st.markdown("* More a company move to the cloud, less it has to deal with responsabilities.")
        st.markdown(" ")
        st.markdown("<u> **Examples** : </u>", unsafe_allow_html=True)
        st.markdown("* In a **SaaS** product such as **gmail**, you can receive, send and store your mails regardless "
                    "of underlying programs or storage space.")
        st.markdown("* In a **PaaS** product such as **[Databricks](https://databricks.com/)**, you can select your "
                    "computation marchines, but you don't have to config them.")
        st.markdown("* In a **IaaS** product such as **AWS**, you can manage your activity without developing by "
                    "yourself the servers, storage and networking.")

    st.subheader('Azure Deployment Models')
    st.markdown('Azure allows users several kind of deployment models for their SI :')
    col1, col2 = st.columns((1, 2))
    with col1:
        st.markdown(' ')
        st.markdown(' ')
        st.markdown('* **Public Cloud** : Everything is build on the cloud provider (Known as **Cloud Native**)')
        st.markdown("* **Private Cloud** : Everything is build on company's datacenter (Know as **On-premise**)")
        st.markdown('* **Hybrid** : Both on premise and on the cloud service provider')
        st.markdown('Here you will find a resume table of the pro and cons about the different deployments models :')
        st.markdown(
            '* **Cross-cloud** : it is such as hybrid cloud but by combining multiple cloud providers (ex: AWS and GCP)')
    with col2:
        table_comparaison_deployement_models = Image.open('images/table_comparaison_Deployement_models.PNG')
        st.image(table_comparaison_deployement_models,use_column_width=True)

    st.subheader('Total cost on the Ownership (TCO)')
    st.markdown('Generally, the **user/client saves 75% of his expenses** when he moves from on-premise to the cloud.')

    st.subheader('CAPEX vs OPEX')
    st.markdown(
        '**CAPEX Capital Expenditure** : Spending money on physical infrastructure (Servers/Storage/Network/Backup/Disaster prevention/Data center costs).')
    st.markdown(
        '**OPEX Operational Expenditure** : Cost associated with a on-premise datacenter that has shifted to the service provider(Training on cloud services/Paying for cloud support/ billing for loud support etc.).')

    st.subheader('Cloud Architecture Terminologies')
    st.markdown('* **Avaibility** : Ensure that service remains available (**HA = Highly available**).')
    st.markdown('* **Scalability** : Can grow rapidly or unimpeded.')
    st.markdown('* **Elasticity** : Ability to shrink and grow to meet the demand.')
    st.markdown('* **Fault Tolerance** : Ability to prevent a failure.')
    st.markdown('* **Disaster Recovery** : Ability to recover from a failure (** DR= Highly Durable**).')
    st.markdown('You can note that, by insisting on these terminologies, Microsoft Azure wants to provide a **plateform highly configurable and stable by the time**.')


    st.subheader('Highly available')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('![regions_balancer_illustration](https://docs.microsoft.com/fr-fr/azure/load-balancer/media/cross-region-overview/cross-region-load-balancer.png)')
    with col2:
        st.markdown('Your services remain available even if there is a failure. It assume a certain level of performance.')
        st.markdown(
            '**Azure Load Balancer** : Azure give you the ability to distribute traffic to multiple servers in datacenters.'
            'You will find it as an illustration just to the left.')

    st.subheader('High scalability')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            'This is the ability to increase your capacity base on the demand of **traffic**, **memory** and **computing power**.')
        st.markdown('You have 2 types of scaling :')
        st.markdown('* **Vertical Scaling** : Upgrade to a bigger server')
        st.markdown('* **Horizontal Scaling** : Distribute traffic to multiple servers')
    with col2:
        st.image('https://www.section.io/assets/images/blog/featured-images/horizontal-vs-vertical-scaling-diagram.png',use_column_width=True)

    st.subheader('High Elasticity')

    st.markdown('This is the ability to automatically increase or decrease traffic,memory and computing power')
    st.markdown('To to that, we can add more server anytime by **horizontal scaling **')
    st.markdown('* **Scaling out** : Adding more servers of the same size')
    st.markdown('* **Scaling in** : Removing more servers of the same size')
    st.markdown('You can use **Azure VM Scale Sets** that automatically increase or decrease in demand')


    st.subheader('High durability')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('Your abaility to recover from a disaster and prevent the loss (**Disaster Recovery DR**)')
        st.markdown('* Do you have a backup ?')
        st.markdown('* How fast can you restore that backup ?')
        st.markdown('* Does your backup stillwork ?')
        st.markdown('* How do you ensure current live data is not corrupt ?')
    with col2:
        st.markdown(':arrow_forward: In order to avoid issues and disaster, Azure allows you to choose a **redundant option** :')
        st.markdown('1) Redundancy in your primary region')
        st.markdown('* **Locally reundant storage (LRS)** : copies your data synchornously **3 times in a single location** in your primary region (least expensive).')
        st.markdown('* **Zone-redundant storage (ZRS)** : copies your data across 3 Azure availability zones in the primary region (for applications requiring high availability).')
        st.markdown('2) Redundancy in your secondary region')
        st.markdown('* **Geo-redundant storage (GRS)** : Such as **LRS** but copy also in a secondary region.')
        st.markdown('* **Geo-zone-redundant storage (GRZS)** : Such as **ZRS** but copy also in a secondary region.')


    st.subheader('Evolution of Computing :')
    col1, col2 = st.columns(2)
    with col1:
        evolution_computing = Image.open('images/dedicated_servers.PNG')
        st.image(evolution_computing,use_column_width=True)
        container_computing = Image.open('images/container_computing.PNG')
        st.image(container_computing, use_column_width=True)
    with col2:
        VM_computing = Image.open('images/virtual_machines.PNG')
        st.image(VM_computing, use_column_width=True)
        function_computing = Image.open('images/function_computing.PNG')
        st.image(function_computing, use_column_width=True)

    st.subheader('Global infrastructure - Regions and Geographies')
    st.markdown(' A region is a group of multiple datacenter')
    st.markdown('* Azure has **58 Regions** across **140 countries**')
    st.markdown('* Azure come from USA but it has several data center across the world, such as Ireland for the Europe')

    st.markdown(
        ' Each region is paired with another 300 miles aways, it enable Disaster Recovery by replicating the data to a secondary region automaticaly (**Azure Geo-redundant Storage GRS**)')

    st.subheader(' Global infrastructure - Region Types and service Avaibility')
    st.markdown('Not all cloud services are available in every regions')
    st.markdown('* **Recommanded Regions** : Region designed to support avaibility zones')
    st.markdown('* **Alternate (other) region** : A region not designed to support Azure zone services.')
    st.markdown('* **General Avaibility GA** : Is when a service is considered ready to be used publicly by everyone')
    st.markdown('Azure cloud services are grouped into 3 categories :')
    st.markdown('* 1) ** Foundational** : when GA, available immediately or in 12months')
    st.markdown(
        '* 2) **Mainstream** : When GA, available immediately or in 12 months. May become avaialbe in alternate regions based on customer demand')
    st.markdown('* 3) **Specialized** : Avaiable in recommended or alternate demand based on customer demand.')

    st.subheader(' Global infrastructure - Special Regions')
    st.markdown(' Azure has specialized regions in order to meet **compliance or legal reasons**.')
    st.markdown(' If you want to learn more about these regions, we suggest to you click [here](https://docs.microsoft.com/en-us/azure/virtual-machines/regions#special-azure-regions).')

    st.subheader(' Global infrastructure - AZ Avaibility zone')
    col1, col2 = st.columns(2)
    with col1:
        st.image('https://docs.microsoft.com/fr-fr/azure/availability-zones/media/availability-zones.png',use_column_width=True)
    with col2:
        st.markdown(' Azure has many datacenter, in a data center you will find hundred of computers.  ')
        st.markdown(' A region contain generally 3 avaibility zones')
        st.markdown('It is common practice to run workloads in at leats 3 AZs. It is important to process like that, because if a **failure appear, nothing will be lose thanks to the redundancy between the Azure Avaibility zones**.'
                    'Each availability zones are connected by high-performance network with a round-trip latency of less than 2ms. Theses **Availability zones are designed so that if one zone is affected, regional services, capacity and availability are supported by the other remaining zones.')

    st.subheader('Global infrastructure - AZ supported Regions')
    st.markdown(
        'Not every regions has support for Avability zones => regions "alternate" or "other. Recommanded regions **are supposed to have at least 3AZs**')

    st.subheader('Global Infrastructure - Availability with fault domains and update domains')
    st.markdown('What is an **availability set** ?')
    st.markdown(':arrow_right: Availability Sets ensure that the **Azure virtual machines are deployed across multiple isolated hardware nodes in a cluster**. It provides redudancy for your virtual machines.')
    st.markdown('There is 3 main scenario that can damage your VMs :')
    st.markdown('* Unplanned hardware maintenance')
    st.markdown('* Unexpected downtime')
    st.markdown('* Planned maintenance')
    st.markdown(' Note that after all planned and unplanned events, your VMs and OS will be rebooted.')
    st.markdown(' Each VMs in your availability set is assigned an **Update domain** and a **Fault Domain**')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('* **Fault domain** : logical group of hardware to avoid single point of failure. A network of VM share a common power source and network switch.')
        st.image('https://csharpcorner-mindcrackerinc.netdna-ssl.com/article/availability-set-fault-domains-and-update-domains-in-azure-virtual-machie/Images/Screenshot_26.png', use_column_width=True)
    with col2:
        st.markdown('* **Update domain** : Constantly applying updates to the underlying hardware and software.')

    st.markdown('<u>**Remember that** :</u>', unsafe_allow_html=True)
    st.markdown('* you need to create VMs **in the same resource group as the availability set.')
    st.markdown('* 1 VM can only be in 1 Availability set.')
    st.markdown('* You can asign VM to the availability set **only during the creation of virtual machines**.')
    st.markdown('* You should create separate storage account for each VM.')


    st.subheader('Computing services')
    st.markdown('* **Azure VM** : common type to compute (OS memmory CPU storage)')
    st.markdown('* **Azure Container instances** : Docker container to deploy app')
    st.markdown('* **Azure Kubernetes service AKS** : deploy manage and scale containerized applications')
    st.markdown(
        '* **Azure Fabric** : Distributed system plateform, run in azure or on premises => microservices ( easy package deploy manage scalable')
    st.markdown(
        '* **Azure functions** : Event driven serverless compute ( function), run code without managing servers, you pay only for the compute')
    st.markdown('* **Azure batch** : Plan, schedule and execute your batch computer running 100+ jobs in parrallel')

    st.subheader('Azure Storage Services')
    st.markdown('* **Azure blob storage** : serverless storage, can store everything, you pay for what you consume.')
    st.markdown('* **Azure Disk Storage**: Hard drive in the cloud, SSD or HDD.')
    st.markdown('* **Azure File Storage** : You can manage it like servers SMB')
    st.markdown(
        '* **Azure Queue Storage** : Messaging queu a data store for reliably delivering messages between applications')
    st.markdown('* ** Azure Table storage ** : No SQL database that stored unstructured data')
    st.markdown('* **Azure Databox / Azure Databox Heavy** : Used to move terabyte or petabytes of data')
    st.markdown('* **Azure Archive** : Long term storage for old files, its cheaper')
    st.markdown(
        '* **Azure Data Lake **: centralized repository that allows to store structred and unstrucured data at any scale.')

    st.subheader('Azure DataBase services')
    st.markdown('* **Azure cosmos DB ** : NoSQL Database, for scale and 99,999999% avaibility')
    st.markdown(
        '* ** Azure SQL DataBase ** : Fully managemed MS SQL with auto scale, robust security and incredible performance')
    st.markdown('* ** Azure DB MSQL PSQL MariaDB** : Fully managed and scalable with hight aivaibility and security')
    st.markdown('* **SQL servers on VMs** : On premise to azure cloud')
    st.markdown('* **Azure synapse Analytics** : Fully managed data warehouse with integral security at no extra cost')
    st.markdown(
        '* **Azure database migration service** : migrate your database to the cloud with no application code changes')
    st.markdown(
        '* **Azure cache for redis** : Caches frequently used and static data to reduce data and application latency')
    st.markdown('* ** Azure table storage** : NoSQL database unstructured and no any scheme')

    st.subheader('Application Integration Services')
    st.markdown('its the glue of service , it make interation between applications')
    st.markdown('* **Azure Notification Hub** : Pub/Sub send push notif to any plateform any backend')
    st.markdown('* **Azure API apps** : API gateway quicly build and consume API in the cloud')
    st.markdown(
        '* **Azure Service Bus** : Service bus cloud messaging as a service (Maas) simple and hybrid integration')
    st.markdown('* **Azure stream Analytics** : Serverless Real time analystics , from the cloud to the edge')
    st.markdown('* **Azure Logic Apps** : Schedule, automate and orchestrate tsks, business process and workflows.')
    st.markdown(
        '* **Azure API management** : Hybrid, multiple cloud management plateform for APIs across all environments. Can be put in addition of an existing API')
    st.markdown('* **Azure Queueue Storage** : Messaging queue delivering message between applications ')

    st.subheader('Developer and Mobile Tools')
    st.markdown(
        '* **Azure SignalR Service** : Real time messaging easily add real-time web functionnality to applications')
    st.markdown(
        '* **Azure App Service** : Easy deloy and scaling application .Net Node.js java, python and php develloper')
    st.markdown('* **Azure Visual studio** : IDE powerfull, scalable applications for Azure')
    st.markdown('* **Xamarin** : Mobile-app framework create powerfull mobile app')

    st.subheader('Azure Devops Services')
    st.markdown('Azure Devops: Plan, collaborate, etc its a repo but with much more tools.')
    st.markdown('* **Azure Boards ** : Kaban deliver value to your users => plan tracks and discuss.')
    st.markdown('* **Azure Pipelines** : Build test and deploy CI/CD with any language')
    st.markdown('* **Azure repos** : Cloud hosted private repos')
    st.markdown('* ** Azure Test Plans** : Test and ship with confidence using manual and exporatory testing tools')
    st.markdown('* **Azure Artifacts** : Create, host ,and share packages with your team, add CI/CD in a single click ')
    st.markdown('* **Azure Devtest Labs** : dev-test environnements. ')

    st.subheader('Azure Resource Manager')
    st.markdown('What is Infrastructure as Code (IaC) ?')
    st.markdown('=> lauching/managing processes by definitions files (such as launching VM via Json file)')
    st.markdown(
        '* **Azure Resource Manager (ARM)** : Allows you to programmatically create Azure ressource via Json template.')

    st.subheader('Azure Quickstart templates')
    st.markdown(
        ' It is a library of a pre-made ARM templates provided by the community to help you laucnh new project (such as repo deployement template).')
    st.markdown('It is pre wrorte scripts')

    st.subheader('Azure Virtual Networks (vNet) and Subnets')
    st.markdown(
        '** Virtual Networks Vnets is a logically section isolated of the Azure network. You choose a range of IPs using CIDR Range. Private subnet. Subnets need to have a smaller CIDR range to the Vnet, we can setup an IP range (65536 IP adresses)')
    st.markdown('* Public subnet : can reach internet')
    st.markdown('* Private Subnet : Cannot Reach internet')

    st.subheader('Cloud-Native Networking Services')
    st.markdown('* **Azure DNS** : Provide ultra fast DNS responses')
    st.markdown(
        '* **Azure Virtual Networks (Vnet)** : A logical isolated section of the Azure network for customers to launch ressources with it')
    st.markdown('* **Azure Load Balancer** : OSI lvl 4 (transport) load balancer')
    st.markdown('* **Azure application gateway** : OSI lvl 7 HTTP load balancer, can apply a web application firewall')
    st.markdown('* ** Network security groups** : a virtual firewall at the subnet level.')

    st.subheader('Enterprise / Hybrid Networking Services')
    st.markdown('* **Azure Front Door** : Scalable and secure entry point for fast delivery of yur global applications')
    st.markdown(
        '* **Azure Express Route** : This is a connexion between your on-premise to Azure Cloud from 50Mbps to 10 Gbps')
    st.markdown(
        '* **Virtual WAN** : A networking service that brings many networking, seurity and routing functionalities together to provide a single operational interface.')
    st.markdown('* **Azure Connection** : A VPN connection securely connects two Azure local network via (IPsec).')
    st.markdown(
        '* ** Virtual Network Gateway** : A site-tosite VPN connexion between Azure virtual machine and your local network.')

    st.subheader('Azure Trafic Manager')
    st.markdown(
        'It operates at the **DNS Layer** to quickly and efficiently direct incoming DNS requests based on the **routing method of you choice**.')

    image_azure_trafic_manager = Image.open('images/Azure Trafic manager.PNG')
    st.image(image_azure_trafic_manager)

    st.subheader('Azure DNS')
    st.markdown(
        ' Azure DNS allows you to host your domains names on Azure. You can create DNS zones and manage your DNS records.')
    st.markdown('**PS** : Azure DNS does not allow you to purchase domains.')

    st.subheader('Azure Load Balancer')
    st.markdown(
        'It is used for evenly distributing incoming network traffic across a group of backend resources or servers.')
    st.markdown('Azure Load Balancer operates on OSI layes 4 (Transport).')
    st.markdown('You can create :')
    st.markdown(
        '* **A public Load Balancer** Incoming traffic from the internet to **public-facing servers** (Public IPs)')
    st.markdown(
        '* **Internal (private) Load Balancer incoming internal network traffic to **private-facing servers** (Private IPs)')

    st.subheader('Scale Sets')
    st.markdown(
        ' Allows to group identical virtual machine in order to autimatically increase or decrease the amount of servers based on : ')
    st.markdown('* Change CPU, Memory, Disk and network performance')
    st.markdown('* On a predefined schedule')

    st.subheader('IoT Services')
    st.markdown('What is IoT ?')
    st.markdown(
        ' IoT => Internet of things : it is a network of internet connected objects (usually hradwares) able to collect and exchange data')
    st.markdown('Ex: Alexa, Smart Fridges, Smart lights, Drones, Phones etc ...')

    st.markdown('In Azure you will find the following Azure IoT Services:')
    st.markdown('* **IoT Central** : Connect your IoT devices to the Cloud')
    st.markdown(
        '* **IoT Hub** : Enable Highly secure and reliable communication between your IoT application and devices it manage')
    st.markdown(
        '* **IoT Edge** : Fully managed service build on Azure IoT Hub. It allows data processing and analysis nearest the IoT devices.'
        'Edge computing is when you offload compute from the cloud to local computing hardware such as IoT devices, phones or home computers.')
    st.markdown(
        '* ** Windows 10 IoT core services** : it is a cloud services subscription that provides the essential services needed to commercialize a device on windows 10 IoT core')

    st.subheader('Big Data and Analytics Services')
    st.markdown('What is Big Data ?')
    st.markdown('It is used to describle massive volume of strucutre or unstructured data')

    st.markdown(
        '* **Azure Synapse Analytics** : Enterprise Data wharehouse used to run SQL queries and also do some reportings on the data')
    st.markdown('* **HDInsight** : Run open-source analytics software such as hadoop, kafla and spark')
    st.markdown('* **Azure Databricks** : Apach spark plateforme optimized for big data computing by using spark')
    st.markdown(
        '* **Data Lake Analytics** : It is an on demand job service that simplify big data. It is a storage repository that can hold data in native format.')

    st.subheader('AI / ML Services')
    st.markdown('What is Aritificual Intelligence ? ')
    st.markdown('It is Machine that perform mimic human behavior')
    st.markdown('What is Machine Learning ? ')
    st.markdown(' Machines that get better at task without explicit programming ')
    st.markdown(' What is Deep Learning ?')
    st.markdown(' Neural network inspired by human brain to solve complex problems')

    st.markdown(
        '* **Azure Machine Learning Service** : A service that simplifies running AI/ML taks using flexible pipeline, you can use R, Python and run DL workloads such as Tensorflow')
    st.markdown(
        '* **Azure Machine Learning Studio** : A service that manage IA ML workloads. Does not have a pipeline and other limitations. ')

    st.subheader('AI/ML Services')
    st.markdown('* **Personalizer** : Deliver rich personnaliser experience for users.')
    st.markdown('* **Translator** : Add real-time, multi-language text translation to your apps, website and tools.')
    st.markdown('* **Anomaly detector** : Detect anomalies in data to quickly identity and troubleshoot issues.')
    st.markdown('* **Azure Bot Service ** : Intelligent, serverless bot service that scales on demand.')
    st.markdown('* **Form recogniser** : Automate the extraction of text, key/value from documents and table.')
    st.markdown('* **Computer vision** : Easily customise computer vision models for your unique use case.')
    st.markdown('* **Language Understanding** : Build NLP into apps, bots and IoT services.')
    st.markdown('* **QnA Maker** : Conversational question answer bot from your existing content .')
    st.markdown(
        '* **Text Analytics** : Extract information such as sentiment, key phrases, named entities and language from your text.')
    st.markdown('* **Content moderator** : Moderate Text and images to provide safer, more positive user experience.')
    st.markdown('* **Face** : Indentify people and emotions on images')
    st.markdown(
        '* **Ink recogniser** : Recogniser digital ink content, such as handwriting, shapes and document layout')

    st.subheader('Serverless Services')
    st.markdown('What is serverless ?')
    st.markdown(
        'It is the underlying servers, infrastructure and OS is taking care of the cloud service provider (CSP). It is generally highly avaiable, scalable and cost-effective.')
    st.markdown('* **Event-Driven Scale** : A serverless function that can be triggered or trigger others event.')
    st.markdown(
        '* **Abstraction of Servers** : Servers are abstracted away. Your code is described as a function. these functions can be running on different compute instances.')
    st.markdown(
        '* **Micro-billing** : Serverless compute could run for afraction of second. Billing into micro-seconds will save you money.')
    st.markdown('Serverless make you save money because you pay for what you consume.')
    st.markdown(
        '* **Azure Functions** : Run small amounts of code known as serverless function in your favoryte language (C#, Python, Java, Javascript, and Powershell')
    st.markdown(
        '* **Blob Storage** : Serverless object storage. Just upload files and don"t think about the underlying systems')
    st.markdown(
        '* **Logic Apps** : Allows you to build serverless workflows composed of Azure functions Building a state machines for serverless compute.')
    st.markdown(
        '* **Event grid** : Uses Pub/Sub messaging system to allow you react to events and trigger other azure cloud services such as Azure functions.')

    st.subheader('Azure Portal')
    st.markdown('Is a webbase plateform, it is the entry point of the whole users.')
    st.markdown('**Azure Preview Portal** : Shows the new products, previews, beta or other pre-release.')

    st.subheader('Azure PowerShell')
    st.markdown(
        'It is a task automation and configuration management framework. A command-line shell and a scripting language.')
    st.markdown('We have a set of command in order to manage Azure ressources directly from commands.')

    st.subheader('Azure Visual Studio Code')
    st.markdown('It is a free IDE mqde by Microsoft for windows, Linux and Mac OS')

    st.subheader('Azure Cloud Shell')
    st.markdown(
        'Brower accessible shell to manage azure ressources. It provide flexibility of choosing the shell. You can do either Bash or PowerShell.')

    st.subheader('Azure CLI')
    st.markdown('What is Azure CLI ?')
    st.markdown(
        '**Azure Command Line Interface (CLI)** processes commands to a computer program in the for of lines of text. Operating systems implement a command-line interface in a shell or terminal.')
    st.markdown(
        'It can be installed on windows, mac and Linux. Once installed, you can type **az** as a command line followed by other commands to create, update, delete, view and manage Azure resources.')

    st.subheader('Create a resource group')

    st.subheader('Create a VNet (Virtual Network)')

    st.subheader('Lauching a server')
    st.markdown('We use **Virtual Machine Resource**')

    st.subheader('Creating Azure functions')
    st.markdown('We create a **Function App**')

    st.subheader('Storing file in Blob Storage')
    st.markdown('How to set up **Storage Account**')
    # 2:11:06/ 3:10:25
