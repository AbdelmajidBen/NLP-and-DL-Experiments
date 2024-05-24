# LAB 4

## Project Overview

This project involves the collection and analysis of text data from the web, focusing on Formula 1 and information about AI Oracle/AWS text generation (based on GPT-2) and Amazon reviews using BERT. The project is divided into three parts:

1. **Data Collection and Preparation**: Scraping text data related to Formula 1 and AI Oracle/AWS using BeautifulSoup.
2. **Text Generation**: Using a fine-tuned GPT-2 model to generate stories based on the data.
3. **Model Evaluation and Contributions**: Training various models with the collected data and acknowledging the support from contributors.

## Part 1: Data Collection and Preparation of the Pipeline and Training the Models

### Objective
Collected the text data from several websites related to Formula 1 and AI in Arabic, and prepared a clean dataset for analysis using an NLP pipeline (Tokenization, stemming, lemmatization, stop words removal, discretization, etc.).

### Tools
- **BeautifulSoup**: A Python library for parsing HTML and XML documents.

### Steps
1. **Data Scraping**:
    - Use BeautifulSoup to scrape text data from relevant websites.
    - Focus on collecting data about Formula 1 races, teams, drivers, and technology.
    - Gather information on AI from Oracle/AWS, focusing on their applications and impact.

2. **Dataset Preparation**:
    - Organize the collected data into a structured format.
    - Each entry should include the text and a relevance score between 0 to 10.

3. **Pipeline Establishment and Model Training**:
    - Establish an NLP pipeline for preprocessing the collected data.
    - Train models using RNN, Bidirectional RNN, GRU, and LSTM architectures.
    - Tune hyper-parameters to achieve the best performance.
    - Evaluate the models using metrics like Mean Absolute Error (MAE), Accuracy, and Loss.

## Part 2: Text Generation with GPT-2

### Objective
Fine-tune a pre-trained GPT-2 model on the collected dataset and generate new paragraphs based on given sentences.

### Tools
- **PyTorch-Transformers**: A library for working with pre-trained transformer models.
- **GPT-2**: A state-of-the-art text generation model by OpenAI.

### Steps
1. **Model Fine-Tuning**:
    - Install the required libraries and load the GPT-2 pre-trained model.
    - Fine-tune the GPT-2 model on the customized dataset of Formula 1 and AI Oracle/AWS text data.
    - Note: This part was run on Google Colab due to the requirement of a proper GPU. Running on a CPU would take approximately 5 hours for fine-tuning.

2. **Text Generation**:
    - Generate new paragraphs according to given sentences, focusing on creating coherent and contextually relevant text.

## Part 3: Model Evaluation and Contributions

### Objective
Train and evaluate different models using the collected data, and acknowledge the contributions from helpers and supporters.

### Tools
- **PyTorch**: A deep learning framework for building and training models.
- **Pre-trained Models**: Such as BERT and GPT-2.

### Steps
1. **Model Training**:
    - Train models using architectures like RNN, Bidirectional RNN, GRU, and LSTM.
    - Tune hyper-parameters to achieve the best performance.

2. **Evaluation**:
    - Evaluate the models using standard metrics (Accuracy, Loss, F1 score) and other relevant metrics like BLEU score.
    - Provide a general conclusion on the use of pre-trained models like BERT for this task.
    - Discuss using BERT for analyzing Amazon reviews, focusing on its effectiveness in sentiment analysis and review summarization.

3. **Acknowledgements**:
    - Recognize the contributions and support from various individuals who helped in completing this project.

## Contributors

Special thanks to the following individuals for their help and support:
- DANIEL BELTSAZAR MARPAUNG


## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```


## Conclusion

This project provides an end-to-end solution for scraping, preparing, and analyzing text data related to Formula 1 and AI Oracle/AWS. It demonstrates the use of various NLP models and highlights the importance of fine-tuning pre-trained models for specific tasks. Additionally, it explores the use of BERT for analyzing Amazon reviews, showcasing its capabilities in sentiment analysis and text summarization.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please contact [abdelmajidbenjelloun5@gmail.com](mailto:abdelmajidbenjelloun5@gmail.com).

---

Université Abdelmalek Essaadi, Faculté des Sciences et Techniques de Tanger, Département Génie Informatique, Master AISD, NLP Lab Project.
