# Nordhealth AI Recruitment Task

## Background

Provet Cloud, our main product, is our SaaS suite of tools required to run veterinary practice.

One of the features (& most common workflows) is consultations. During a scheduled appointment our users can fill in 
patients consultation cards with all details regarding that consultation - this can be the medicine administered, 
treatments performed, observation notes, etc.

After the patient is done with the consultation he usually recieves discharge notes - a set of simple instructions 
summarizing what happened during the consultations and what are the next steps the patient should take.

## Your task

Writing these discharge notes is mundane and takes time. Your task is to automate it.

Write a script that uses a LLM to automatically generate discharge note given the consultation data. Your script should 
accept only one argument: a path to a JSON file containing data from a consultation.

It should output a JSON that contains the key `discharge_note`, for example:

```json
{
  "discharge_note": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ..."
}
```

You have a few examples in the `data/` directory which you can use to test your solution.

Solving this problem should take you no more than 2 hours.

## Requirements

* You can use any LLM provider of your choice
* For each test file in `data/` please include a corresponding output json file in `solution/`.
* Once you're done please create submit your solution to a github/gitlab repository and provide us with the link.
* API tokens to LLM provider should NOT be committed to the repository. 
  Your script should read them from environment variables or a config file.

For all things that you come up with that aren't covered within the requirements above - we trust your judgement to 
make the right decision. The solution is not meant to be perfect, but please 


## Notes on the development process

- The GitHub Actions have a lot of duplication but for a effort/gain perspective I decided to keep them as is now. They work and can be optimised, cached later;
- I have chosen to read only a subset of the consultation data to objects instead of passing the whole data file because the data file can potentially containt PII/sensitive data and not everything needs to be passed to an LLM;
- I am aware that consultation1.json has an error, ie an additional comma. To ensure the parsing strategy is a bit more "forgiving" I have chosen to use json5 instead of simply reading the json data. This is a deliberate choice to ensure the end users get some response even if the data format is not strictly right;


## Future Development Opportunities

- Depending on how this is meant to integrate in a production setting in the existing product, there are many ways to evolve this. 
  - If this is really file based, you could set up a trigger on a file being placed in s3 and trigger a Lambda function (examples in AWS but this can be easily translated to other cloud providers) to generate a file and land it in the desired location;
  - If this is part of a service, you would probably want to expose a RESTful API, e.g., FastAPI or equivalent to receive the input data, do the data processing and LLM calls and process them into a sensible response specified in an OpenAPI specification or equivalent;
  - Since this does seem time sensitive, a batch job approach does not seem like a good fit for this use case;
- I have found that demos tend to be quite useful, so either adding a small StreamLit demo on top of this or simply exposing a Swagger interface, could be great for this purpose;
- For LLMs, it is essential to think about what happens when things go wrong, e.g., hitting quotas or if the third party LLM provider is down. What is the fallback strategy? Do you retry a few times (and with what retry logic) and then pivot to a different LLM? Or do you also maintain a more rudementary fallback option, just repeating the key parts of the consultation data?