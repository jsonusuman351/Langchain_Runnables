# ⛓️ Exploring LangChain Runnables (LCEL)

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![FAISS](https://img.shields.io/badge/FAISS-0080FF?style=for-the-badge)

Hey there! Welcome to my exploration of **LangChain Runnables** and the **LangChain Expression Language (LCEL)**. After working with the older `Chains` interface, I wanted to dive into this newer, more flexible way of building AI workflows. The "pipe" (`|`) syntax isn't just for looks; it makes building complex, production-ready applications much more intuitive.

This repository is basically my personal journey and a collection of scripts where I break down how to use the most important `Runnable` components to create everything from simple sequences to a full-blown Retrieval-Augmented Generation (RAG) system.

---

### 🤔 Why Runnables? A Quick Note

Before diving in, I wanted to share why I focused on this. The LCEL and `Runnable` protocol are the future of LangChain. They offer huge advantages:
-   **Streaming Support**: You can stream outputs token-by-token, which is amazing for creating responsive chat UIs.
-   **Asynchronous Operations**: Easily run chains with `async` and `await` for better performance.
-   **Parallel Execution**: Run parts of your workflow at the same time, which I've explored in one of the scripts.
-   **Automatic Tracing**: LangChain automatically tracks every step of your Runnable sequence, which is a lifesaver for debugging.

---

### ✨ Core Concepts I've Explored

Here’s a breakdown of the key `Runnable` components I've implemented in this repository:

1.  **`RunnableSequence` (`runnable_sequence.py`)**:
    -   This is the most fundamental concept. I started here to understand how to pipe components together: **Prompt ➔ Model ➔ Parser**. It's the modern way to do what `SimpleChain` used to do.

2.  **`RunnablePassthrough` (`runnable_passthrough.py`)**:
    -   This one was a real "aha!" moment. It lets you pass inputs through a chain unchanged, which is crucial for RAG. I built a simple RAG chain here that takes a question, fetches relevant documents, and then "passes through" both the original question and the retrieved documents to the next step.

3.  **`RunnableParallel` (`runnable_parallel.py`)**:
    -   Just like with the older chains, this lets you run multiple operations at the same time and get a combined dictionary output. I used it to create a chain that takes a topic and simultaneously generates both a question and a joke about it.

4.  **`RunnableBranch` (`runnable_branch.py`)**:
    -   This is how you add conditional logic or "if/else" statements to your workflows. I created a chain that first classifies a user's question as either "Math" or "General Knowledge" and then routes it to a specialized chain for the correct answer.

5.  **Putting It All Together: A Full RAG Chain (`retrievalQAchain.py`)**:
    -   This script is the final boss of this repository. It combines everything I learned to build a complete Retrieval-Augmented Generation (RAG) system. It takes a user's question, finds relevant information from a text file, and uses that context to generate an informed answer.

---

### 🛠️ Tech Stack

-   **Core Framework**: LangChain & LangChain Expression Language (LCEL)
-   **LLM Provider**: OpenAI
-   **Vector Store**: FAISS (for in-memory semantic search in the RAG chain)
-   **Core Libraries**: `langchain-core`, `langchain-openai`, `python-dotenv`

---

### ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jsonusuman351/Langchain_Runnables.git](https://github.com/jsonusuman351/Langchain_Runnables.git)
    cd Langchain_Runnables
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   Create a file named `.env` in the root directory.
    -   Add your OpenAI API key to this file:
        ```env
        OPENAI_API_KEY="your-openai-api-key"
        ```

---

### 🚀 How to Run the Scripts

Each script is a standalone example. Feel free to run them and see how each `Runnable` works.

-   **Basic Chaining:**
    ```bash
    python runnable_sequence.py
    ```
-   **Chaining with Passthrough (for RAG context):**
    ```bash
    python runnable_passthrough.py
    ```
-   **Parallel Execution:**
    ```bash
    python runnable_parallel.py
    ```
-   **Conditional Logic:**
    ```bash
    python runnable_branch.py
    ```
-   **RAG System:**
    *Make sure you have a PDF file in your project directory for this to work.*
    ```bash
    python retrievalQAchain.py
    ```

---

### 🔬 A Tour of My Runnable Experiments

I've organized the scripts based on the core `Runnable` concept they demonstrate.

<details>
<summary>Click to view the code layout</summary>

```
Langchain_Runnables/
│
├── runnable_sequence.py       # The basic "pipe" workflow
├── runnable_passthrough.py    # Passing data through a chain
├── runnable_parallel.py       # Running operations at the same time
├── runnable_branch.py         # Adding if/else logic to chains
├── retrievalQAchain.py        # A complete RAG implementation
│
├── pdf_reader.py              # Helper script for loading PDFs
├── docs.txt                   # Sample text file for RAG
│
├── requirements.txt
├── .env                       # (You need to create this for your API key)
└── README.md
```
</details>

---

---