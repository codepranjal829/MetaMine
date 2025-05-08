import streamlit as st
from streamlit.components.v1 import iframe
st.set_page_config(layout="wide")

# Set up the page configuration
import streamlit as st

# CSS with pastel blue background, button style, and card style
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f8ff; /* Light pastel blue background */
        }

        .stButton>button {
            background-color: #0056b3; /* Dark blue button */
            color: white; /* White text */
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 8px;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background-color: #003d80; /* Even darker blue on hover */
            cursor: pointer;
        }

        .card {
            background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Title + description inside a card
st.markdown("""
    <div class="card">
        <h1 style='text-align: center;'>🧬 MetaMine</h1>
        <p style='text-align: center;'>Welcome to <em>MetaMine</em>, your hub for metagenomics databases and tools.</p>
    </div>
""", unsafe_allow_html=True)




# Resource data (databases and tools)
resources = {
    "databases": {
        "IGM/M": {
            "url": "https://img.jgi.doe.gov/m/",
            "image": "https://pbs.twimg.com/profile_images/1531755125600964608/DSpuI-Uv_200x200.jpg",
            "description": "The Integrated Microbial Genomes (IMG) system serves as a community resource for analysis and annotation of genome and metagenome datasets in a comprehensive comparative context. The IMG data warehouse integrates genome and metagenome datasets provided by IMG users with a comprehensive set of publicly available genome and metagenome datasets."
        },
        "JGI GOLD": {
            "url": "https://gold.jgi.doe.gov/",
            "image": "data:image/png;base64,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",
            "description": "Genomes Online Database, access to genome and metagenome sequencing projects metadata"
        },
        "MGnify": {
            "url": "https://www.ebi.ac.uk/metagenomics/",
            "image": "data:image/jpeg;base64,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",
            "description": "MGnify is a freely available hub for the analysis and exploration of metagenomic, metatranscriptomic, amplicon and assembly data."
        },
        "Human Microbiome Project": {
            "url": "https://hmpdacc.org/",
            "image": "data:image/jpeg;base64,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",
            "description": "NIH's Human Microbiome Project provides comprehensive microbiota data."
        },
        "NMPFamsDB": {
            "url": "https://bib.fleming.gr/NMPFamsDB",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiAwTbi4P77BbGzroY3FEIgRS8fx8efsa40g&s",
            "description": "Database of metagenome- and metatranscriptome-derived protein families with no reference hits."
        },
        "Human Gut Microbiome Atlas": {
            "url": "https://www.microbiomeatlas.org",
            "image": "https://www.microbiomeatlas.org/images_static/microbiome.atlas.logo.svg",
            "description": "Atlas of human oral and gut microbiome data from disease and healthy cohorts."
        }
    },
    "tools": {
        "MetaGeneMark": {
            "url": "https://genemark.bme.gatech.edu/meta_gmhmmp.cgi",
            "image": "https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-3970-61f7-a981-4a255c24102d/raw?se=2025-05-08T11%3A06%3A33Z&sp=r&sv=2024-08-04&sr=b&scid=9ee7bcb1-32bc-5b59-a4e3-f1bc4da2b5fe&skoid=d958ec58-d47c-4d2f-a9f2-7f3e03fdcf72&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-05-08T01%3A17%3A16Z&ske=2025-05-09T01%3A17%3A16Z&sks=b&skv=2024-08-04&sig=3B3ebaas3/cXIV5l2zs1PCZ8A0pu4xb8ZJMBy9UYn5Y%3D",
            "description": "MetaGeneMark is a tool used for identifying protein-coding regions in metagenomic sequences. It's specifically designed for analyzing the DNA fragments found in metagenomes, which are collections of genetic material from various organisms in an environment. MetaGeneMark leverages metagenome-specific parameters and gene prediction programs like GeneMark to locate genes within these short, anonymous sequence fragments"
        },
        "MetaPhlAn": {
            "url": "http://segatalab.cibio.unitn.it/tools/metaphlan3/",
            "image": "http://segatalab.cibio.unitn.it/images/cibiocm_logo.png",
            "description": "MetaPhlAn is a computational tool for profiling the composition of microbial communities (Bacteria, Archaea and Eukaryotes) from metagenomic shotgun sequencing data (i.e. not 16S) with species-level."
        },
        "MG-RAST": {
            "url": "https://www.mg-rast.org/",
            "image": "https://boninabox.geobon.org/images/tool-images/rast1.jpg",
            "description": "A platform for annotation of metagenomic data using Subsystem Technology."
        },
        "MetaThermo":{
            "url":"http://palaeo.nig.ac.jp/metathermo/",
            "image":"https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-4e34-61f7-b264-a7c77136ba67/raw?se=2025-05-08T10%3A12%3A12Z&sp=r&sv=2024-08-04&sr=b&scid=b5093d64-dd42-5346-9354-d10a59ffeb45&skoid=f0c3f613-0f9b-4a8a-a29a-c1a910343ad7&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-05-08T01%3A16%3A38Z&ske=2025-05-09T01%3A16%3A38Z&sks=b&skv=2024-08-04&sig=H3p90k1yCLsI657b4VrG8ql9g0Hc2W9OcdMLMdV/Wuk%3D",
            "description":"Tool for calculate Metagenomic Predicted temperature.Users can upload a fasta or fastq file for shotgun sequencing data and receive a corresponding MPT value."
        },
        "GMGC":{
            "url":"https://gmgc.embl.de/",
            "image":"data:image/png;base64,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",
            "description":"The Global Microbial Gene Catalog is an integrated, consistently-processed, gene catalog of the microbial world, combining metagenomics and high-quality sequenced isolates. A total of 2.3 billion ORFs from 13,174 metagenomes (covering 14 habitats) and the complete ProGenomes2 database were clustered together at 95% nucleotide identity to build a catalog of 302,655,267 unigenes."
        }


    }
}

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = None
if 'type' not in st.session_state:
    st.session_state.type = None

# Function to display embedded content
def display_embedded_content(resource_type, resource_name):
    url = resources[resource_type][resource_name]["url"]
    st.session_state.view = resource_name
    st.session_state.type = resource_type

    st.markdown(f"### 🔬 {resource_name}")
    st.write(resources[resource_type][resource_name]["description"])

    # Button to go back to the list
    if st.button("← Back ", key=f"back_{resource_name}"):
        st.session_state.view = None
        st.rerun()

    
    with st.container():
        try:
            iframe(url, width=2000
                   , height=1000, scrolling=True)
        except Exception as e:
            st.warning(f"Could not load {resource_name} content directly. Check the [official {resource_name} website]({url})")



# Tab structure for navigation
tab1, tab2, tab3,tab4 = st.tabs(["Home", "Databases", "Tools","About"])

# Home Tab
with tab1:
    st.header("Welcome to MetaMine")
    st.write("""
        *MetaMine* is a curated platform bringing together the most important and widely used databases 
        in *metagenomics research*. Instead of overwhelming you with hundreds of sources, 
        we focus on *only the essential databases* that every researcher and student should know.
        
        Our goal is to help you:
        - Quickly find reliable resources
        - Understand each database's focus
        - Explore taxonomic, functional, human microbiome, and resistance datasets

        ---

        #### Why MetaMine?
        - *Handpicked:* Only top trusted databases
        - *Easy Navigation:* Filter by category and keyword
        - *Direct Access:* One-click access to official sites
    """)
    

# Databases Tab
with tab2:
    if st.session_state.view and st.session_state.type == "databases":
        display_embedded_content("databases", st.session_state.view)
    else:
        st.header("📚 Databases")
        for db, details in resources["databases"].items():
            with st.container(border=True):
                col1, col2 = st.columns([1, 5])
                with col1:
                    st.image(details["image"], width=1000)
                with col2:
                    st.write(f"**{db}**")
                    st.write(details["description"])
                    if st.button(f"Browse {db}", key=f"db_{db}"):
                        display_embedded_content("databases", db)
                        st.rerun()

# Tools Tab
with tab3:
    if st.session_state.view and st.session_state.type == "tools":
        display_embedded_content("tools", st.session_state.view)
    else:
        st.header("🛠️ Tools")
        for tool, details in resources["tools"].items():
            with st.container(border=True):
                col1, col2 = st.columns([1, 5])
                with col1:
                    st.image(details["image"], width=1000)
                with col2:
                    st.write(f"**{tool}**")
                    st.write(details["description"])
                    if st.button(f"Access tool {tool}", key=f"tool_{tool}"):
                        display_embedded_content("tools", tool)
                        st.rerun()
    

# About Tab
with tab4:
    st.header("📖 About This App")

    st.subheader("👤Author")
    st.write("""
        The author Pranjal dalvi is currently pursuing a **Master’s in Bioinformatics** at **DES Pune University**.
    Passionate about **metagenomics**, microbiome research, and computational biology.
    Interested in developing user-friendly tools that make biological data analysis more accessible to researchers and students.
    """)

    st.subheader(" 🎯Purpose")
    st.write("""
        This app provides a curated hub of databases and tools for metagenomics research,
        making it easier for researchers to explore resources for microbial community analysis, taxonomic profiling, and functional insights.
    """)

    st.subheader("Key Features")
    st.markdown("""
    - 📚 Curated list of metagenomics databases  
    - 🛠️ Essential tools for microbiome and resistome analysis  
    - 🔬 Embedded views for seamless exploration  
    - 🌍 Beautiful, easy-to-use interface  
    """)
    st.subheader("Benefits")
    st.markdown("""
               Central hub for metagenomics databases and tools

             Saves time by integrating multiple resources in one place

             Easy-to-use, beginner-friendly interface

             Embedded resource viewing without leaving the app

           Educational value for students and early-career researchers 
                
                
                
                """)

    st.subheader("🛠️Tools and Technologies Used")
    st.markdown("""
    - Python  
    - Streamlit    
    - HTML/CSS for styling  
    """)

    st.subheader(" 👨‍🏫 Acknowledgment")
    st.write("""
        I would like to express my heartfelt gratitude to Dr. Kushagra Kashyap, Assistant Professor (Bioinformatics), Department of Life Sciences, School of Science and Mathematics, DES Pune University, for his exceptional guidance and unwavering academic support throughout the development of this project.

        His mentorship has been invaluable in shaping both the scientific vision and technical execution of this work. The continuous encouragement, expert insights, and constructive feedback provided by Dr. Kashyap were key to the successful completion of this mini-project.


    """)

    st.subheader("Feedback")
    st.write("""
        We welcome your feedback! Please share your suggestions or comments at:  
        📧 Email=dpranjal889@gmail.com] 
        
    """)

