
# DataBerry Cluster
## - For a Safe, Secure and Positive Digital World

DataBerry Cluster offers wide range of APIs pertaining to multiple domains primarily built on core vision of problem solving. 

1) DataBerry-QualityAssurance API for **Real-time Data Quality Validation**
2) DataBerry-Detoxifier API for **Toxic Comments Classification**
3) Domain Specific **Sentiment Classification**
4) DataBerry-CleanerAPI for **Automated Data Cleaning and Structuring** 

Choose specific end-points that match your requirements from DataBerry cluster.

## API Reference

### DataBerry Cluster API


| Endpoint        | Method   |   Description              |
| :--------       | :------- | :------------------------- |
| `/text_quality` | `POST`   | Text Quality Assurance API |
| `/personal_identifier`| `POST` | Personal Identifier API |
| `/translate` | `POST` | Text Translator API | 
| `/datacleaner` | `POST` | Text Data Cleaner API | 

### 1) Text Quality Analysis API
Given a text input, the API will return 
- Query Language
- Number of Words
- Query Length
- Toxicity Level / Score
- Text Sentiment Score

### 2) Personal Identifier API
Given a text input, the API will extract all `personal information` such as
- Dates (Y-M-D Format)
- Email
- Gender
- Names
- Geo-location
- Phone Number

### 3) DataBerry Cluster Cleaner API
Given a text input, the Cleaner API will remove unwanted `stopwords`, `html tags` and `user-defined words` from the input text.
