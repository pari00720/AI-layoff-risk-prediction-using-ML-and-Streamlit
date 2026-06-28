"""
Role-based AI career recommendations.

This file contains recommendations that are displayed after
prediction. It does NOT affect the ML model.
"""

ROLE_RECOMMENDATIONS = {

    "Academic Coordinator": {
        "medium": {
            "skills": [
                "AI in Education",
                "Digital Administration",
                "Prompt Engineering",
                "Data Management"
            ]
        },
        "high": {
            "skills": [
                "AI in Education",
                "Learning Management Systems",
                "Prompt Engineering",
                "Educational Analytics",
                "Leadership"
            ],
            "certifications": [
                "Google AI Essentials",
                "Microsoft AI-900"
            ]
        }
    },

    "Accountant": {
        "medium": {
            "skills": [
                "Advanced Excel",
                "Power BI",
                "Financial Analytics",
                "AI for Finance"
            ]
        },
        "high": {
            "skills": [
                "Power BI",
                "Python for Finance",
                "Financial Analytics",
                "Automation Tools",
                "AI for Accounting"
            ],
            "certifications": [
                "Google Data Analytics",
                "Microsoft AI-900",
                "Google AI Essentials"
            ]
        }
    },

    "Auditor": {
        "medium": {
            "skills": [
                "Risk Analytics",
                "Power BI",
                "AI-assisted Auditing",
                "Data Analysis"
            ]
        },
        "high": {
            "skills": [
                "Fraud Analytics",
                "Python",
                "Power BI",
                "AI Auditing",
                "Data Visualization"
            ],
            "certifications": [
                "Google Data Analytics",
                "Microsoft AI-900"
            ]
        }
    },

    "Data Analyst": {
        "medium": {
            "skills": [
                "SQL",
                "Power BI",
                "Python",
                "Statistics"
            ]
        },
        "high": {
            "skills": [
                "Machine Learning",
                "Generative AI",
                "Cloud Analytics",
                "Advanced SQL",
                "Tableau"
            ],
            "certifications": [
                "Google Data Analytics",
                "Microsoft AI-900",
                "Google AI Essentials"
            ]
        }
    },

    "Dispatcher": {
        "medium": {
            "skills": [
                "Logistics Software",
                "Communication",
                "Scheduling",
                "AI-assisted Routing"
            ]
        },
        "high": {
            "skills": [
                "Supply Chain Analytics",
                "ERP Systems",
                "AI Logistics",
                "Power BI",
                "Automation"
            ],
            "certifications": [
                "Google AI Essentials",
                "AWS Cloud Practitioner"
            ]
        }
    },

    "Financial Analyst": {
        "medium": {
            "skills": [
                "Financial Modeling",
                "Excel",
                "Power BI",
                "Forecasting"
            ]
        },
        "high": {
            "skills": [
                "Python",
                "AI for Finance",
                "Machine Learning",
                "Power BI",
                "Cloud Analytics"
            ],
            "certifications": [
                "Google Data Analytics",
                "Microsoft AI-900"
            ]
        }
    },

    "Health Analyst": {
        "medium": {
            "skills": [
                "Healthcare Analytics",
                "Power BI",
                "SQL",
                "Medical Data"
            ]
        },
        "high": {
            "skills": [
                "Healthcare AI",
                "Medical Informatics",
                "Python",
                "Clinical Analytics",
                "Machine Learning"
            ],
            "certifications": [
                "IBM AI Engineering",
                "Google AI Essentials"
            ]
        }
    },

    "Inventory Analyst": {
        "medium": {
            "skills": [
                "Inventory Planning",
                "Excel",
                "Power BI",
                "Supply Chain"
            ]
        },
        "high": {
            "skills": [
                "ERP Systems",
                "Supply Chain Analytics",
                "Forecasting",
                "AI Inventory Optimization",
                "Automation"
            ],
            "certifications": [
                "AWS Cloud Practitioner",
                "Google Data Analytics"
            ]
        }
    },

    "ML Engineer": {
        "medium": {
            "skills": [
                "Deep Learning",
                "Python",
                "Git",
                "TensorFlow"
            ]
        },
        "high": {
            "skills": [
                "LLMs",
                "MLOps",
                "Vector Databases",
                "RAG",
                "Cloud Deployment"
            ],
            "certifications": [
                "Google AI Essentials",
                "Microsoft AI-900",
                "AWS Cloud Practitioner"
            ]
        }
    },

    "Medical Assistant": {
        "medium": {
            "skills": [
                "Digital Health Records",
                "Healthcare AI",
                "Medical Documentation",
                "Patient Management"
            ]
        },
        "high": {
            "skills": [
                "Medical Informatics",
                "Healthcare Analytics",
                "Clinical AI",
                "Digital Healthcare",
                "Communication"
            ],
            "certifications": [
                "Google AI Essentials",
                "IBM AI Engineering"
            ]
        }
    },

    "Network Engineer": {
        "medium": {
            "skills": [
                "Networking",
                "Linux",
                "Cybersecurity",
                "Cloud Basics"
            ]
        },
        "high": {
            "skills": [
                "Cloud Networking",
                "AWS",
                "Azure",
                "Automation",
                "Network Security"
            ],
            "certifications": [
                "AWS Cloud Practitioner",
                "Microsoft AI-900"
            ]
        }
    },

    "Nurse": {
        "medium": {
            "skills": [
                "Digital Health",
                "Healthcare AI",
                "Communication",
                "Patient Care"
            ]
        },
        "high": {
            "skills": [
                "Medical Informatics",
                "Clinical Decision Support",
                "Electronic Health Records",
                "Healthcare Analytics",
                "Healthcare AI"
            ],
            "certifications": [
                "Google AI Essentials",
                "IBM AI Engineering"
            ]
        }
    },

    "Operations Analyst": {
        "medium": {
            "skills": [
                "Excel",
                "Power BI",
                "Operations Research",
                "SQL"
            ]
        },
        "high": {
            "skills": [
                "Process Automation",
                "Data Analytics",
                "Cloud",
                "Machine Learning",
                "Business Intelligence"
            ],
            "certifications": [
                "Google Data Analytics",
                "AWS Cloud Practitioner"
            ]
        }
    },

    "Operator": {
        "medium": {
            "skills": [
                "Machine Operations",
                "Quality Control",
                "Safety",
                "Automation Basics"
            ]
        },
        "high": {
            "skills": [
                "Industrial Automation",
                "PLC Basics",
                "Manufacturing Analytics",
                "AI Manufacturing",
                "Maintenance"
            ],
            "certifications": [
                "Google AI Essentials"
            ]
        }
    },

    "Production Supervisor": {
        "medium": {
            "skills": [
                "Lean Manufacturing",
                "Leadership",
                "Quality",
                "Planning"
            ]
        },
        "high": {
            "skills": [
                "Industry 4.0",
                "Manufacturing AI",
                "Automation",
                "Data Analytics",
                "Process Optimization"
            ],
            "certifications": [
                "Google AI Essentials",
                "AWS Cloud Practitioner"
            ]
        }
    },

    "Quality Engineer": {
        "medium": {
            "skills": [
                "Six Sigma",
                "Quality Assurance",
                "Root Cause Analysis",
                "Statistics"
            ]
        },
        "high": {
            "skills": [
                "Predictive Quality",
                "Machine Learning",
                "Manufacturing Analytics",
                "Automation",
                "Python"
            ],
            "certifications": [
                "Google Data Analytics",
                "Microsoft AI-900"
            ]
        }
    },

    "Research Assistant": {
        "medium": {
            "skills": [
                "Research Methods",
                "Python",
                "Statistics",
                "Academic Writing"
            ]
        },
        "high": {
            "skills": [
                "AI Research",
                "LLMs",
                "Machine Learning",
                "Deep Learning",
                "Data Science"
            ],
            "certifications": [
                "Google AI Essentials",
                "IBM AI Engineering"
            ]
        }
    },

    "Sales Associate": {
        "medium": {
            "skills": [
                "CRM",
                "Communication",
                "Digital Sales",
                "Customer Analytics"
            ]
        },
        "high": {
            "skills": [
                "AI Sales Tools",
                "Marketing Analytics",
                "Power BI",
                "CRM Automation",
                "Customer Insights"
            ],
            "certifications": [
                "Google AI Essentials"
            ]
        }
    },

    "Software Engineer": {
        "medium": {
            "skills": [
                "Python",
                "Git",
                "REST APIs",
                "Cloud Basics"
            ]
        },
        "high": {
            "skills": [
                "Generative AI",
                "MLOps",
                "Docker",
                "Kubernetes",
                "Cloud Computing"
            ],
            "certifications": [
                "AWS Cloud Practitioner",
                "Microsoft AI-900",
                "Google AI Essentials"
            ]
        }
    },

    "Store Manager": {
        "medium": {
            "skills": [
                "Retail Analytics",
                "Inventory Management",
                "Leadership",
                "Customer Experience"
            ]
        },
        "high": {
            "skills": [
                "AI Retail",
                "Supply Chain",
                "Business Intelligence",
                "Automation",
                "Power BI"
            ],
            "certifications": [
                "Google AI Essentials",
                "Google Data Analytics"
            ]
        }
    },

    "Supply Chain Analyst": {
        "medium": {
            "skills": [
                "Excel",
                "Forecasting",
                "Inventory",
                "Power BI"
            ]
        },
        "high": {
            "skills": [
                "Supply Chain AI",
                "ERP",
                "Automation",
                "Cloud",
                "Business Intelligence"
            ],
            "certifications": [
                "AWS Cloud Practitioner",
                "Google Data Analytics"
            ]
        }
    },

    "Support Specialist": {
        "medium": {
            "skills": [
                "Technical Support",
                "Communication",
                "Ticketing Systems",
                "Troubleshooting"
            ]
        },
        "high": {
            "skills": [
                "Cloud Support",
                "AI Assistants",
                "Automation",
                "Networking",
                "Customer Success"
            ],
            "certifications": [
                "AWS Cloud Practitioner",
                "Google AI Essentials"
            ]
        }
    },

    "Teacher": {
        "medium": {
            "skills": [
                "AI in Education",
                "Prompt Engineering",
                "Digital Teaching",
                "Canva AI"
            ]
        },
        "high": {
            "skills": [
                "AI in Education",
                "Microsoft Copilot",
                "Prompt Engineering",
                "Educational Analytics",
                "Digital Pedagogy"
            ],
            "certifications": [
                "Google AI Essentials",
                "Microsoft AI-900"
            ]
        }
    },

    "Warehouse Manager": {
        "medium": {
            "skills": [
                "Warehouse Automation",
                "Inventory",
                "Leadership",
                "ERP"
            ]
        },
        "high": {
            "skills": [
                "Supply Chain AI",
                "Power BI",
                "Automation",
                "ERP",
                "Logistics Analytics"
            ],
            "certifications": [
                "AWS Cloud Practitioner",
                "Google Data Analytics"
            ]
        }
    }
}