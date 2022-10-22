# Codes Northwestern

This is a separate folder in this Emotional Support Conversations repo made by researchers at Northwestern HCI+D center. Extending the dataset collected from this ACL paper, we seek to create useful capabilities for (human) help providers to improve their own conversational strategies in real-time. To do this, we are building (1) new detection and suggestion capabilities based on the strategies annotated in the ACL paper; and (2) re-annotating parts of the dataset to support these capabilities.

## Detection Capabilities

One capability we are building is detecting when someone is engaging in "Self-disclosure" strategies too often (e.g., talking about themselves or their own experience in a not helpful way), so that they might direct the conversation to be more about the help seekers problems and experiences.

One problem with this dataset is that the strategy annotations labels are made for a conversational turn, which may contain many different sentences. We saw instance in the dataset which are using multiple strategies at the same time. Thus, we'd like to either label parts of these conversations (e.g., annotate every sentence in the dataset as a span categorization problem; or split the dataset text responses into respective sentences for a text classification problem). 

