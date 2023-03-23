# Question 1
### Problem statement 
The API , mentioned in the documentation is used to create a new template for your company. The API requires certain parameters as inputs and returns an editor link that can be used to create the new template.
### Description 
The mentioned API is designed to facilitate the creation of a new template for your company. To use the API, certain parameters are required to be provided as inputs. Once these parameters are provided, the API generates an editor link that can be used to create the new template. This link will enable you to access the editor interface and customize the template according to your company's requirements. The API provides an efficient and streamlined process for creating templates, which can save valuable time and resources for your company
### Requirements 
- Understand the requirements of the API for creating a new template.
- Write code using any frontend framework based on your understanding of the API.
- Develop a user-friendly interface for a better user experience.
- Once you post the required parameters to the API, it will return an editor link. You can then use that link to display the editor in an iframe.
- Display all templates that have been created in your company and when that is clicked open the template that you have created.
### Notice
You are required to deploy the project on GitHub and complete it within 7 days from the date of question selection. You must share both the codebase link and the deployed link on GitHub. Based on your performance, you will be considered for the next step in the interview process.
### API Documentation
#### API base URL - `https://100094.pythonanywhere.com`
##### Template Management

_POST_ to `templates/`

Request Body

```json
{
    "company_id": "<company_id_of_authenticated_user>",
    "created_by": "<user_name_of_authenticated_user>",
    "data_type":"<get_from_the_login_api>"

}
```

Response-201

```json
 { "editor_link": "<link_to_the_editor>" }
```

Response-300

```json
{ "message": "Template Name is Required" }
```

Response-400

```json
{ "message": "Failed to process template creation." }
```

Response-405

```json
{ "message": "Template Creation failed"}
```

Response 500

```json
{ "message": "Failed to process template creation."}
```

_GET_ `templates/:companyId/`

Response-200

```json
{ "templates": [list of all templates ]}
```
_GET_ `templates/:templateId/`

Response-200

```json
{ "editor_link": "<link_to_the_editor>" }
```

Response-400

```json
{"message": "Failed to fecth template" }
```

Response-404

```json
{"message": "Template Not Found" }
```

Response-500

```json
{"message": "Failed to fecth template" }
```

