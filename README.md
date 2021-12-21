
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
| `/text_quality` | `POST`   | Text Quality Analysis API  |
| `/personal_identifier`| `POST` | Personal Identifier API |
| `/translate` | `POST` | Text Translator API | 
| `/datacleaner` | `POST` | Text Data Cleaner API | 

### 1) Text Quality Analysis API
<p>  Given a text input, the API will return <b>language</b>, <b>number of words</b>,<b>query length</b> (after all empty unwanted white-spaces removed),and <b>toxicity level</b> of input text. </p> 

### 2) Personal Identifier API
Given a text input, the API will extract all `personal information` such as  <b>dates</b>(in y-m-d format), <b>phone number</b>,<b>email</b>,<b>gender</b>.
