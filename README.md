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

## Local setup

1. Clone the repository;
2. Install [poetry](https://python-poetry.org/docs/);
3. Install the relevant dependencies by running `poetry install`;
3. The script uses OpenAI under the hood. For this to work the environment variable `OPENAI_API_KEY` must be set
   provider API key. You can create an OpenAI account and get the API key
   from [here](https://platform.openai.com/settings/organization/api-keys);
4. Run the script with the path to the JSON file as an argument. For example:
   ```bash
   poetry run python main.py data/consultation_1.json
   ```

## Notes on the development process

- The GitHub Actions have a lot of duplication but from an effort/gain perspective I decided to keep them as is now.
  They work and can be optimised, cached later;
- At first, I started by adding data object definitions and validations. However, being conscious of the time limit, I
  chose to keep the current solution simple and simply read in whatever is in the consultation input files. This has
  drawbacks such as passing too much data to the LLM, potentially increasing the latencies. In this specific case I am
  not concerned about PII data because Enterprise subscriptions specifically state that the prompt data is not persisted
  or used for model training.
- I am aware that consultation1.json has an error, ie an additional comma. However, reading in the file contents as a
  string allows me to get information out of an otherwise imperfect JSON file. You could argue it is a tradeoff to
  deliver as many responses as possible to the user in an attempt to minimise frustration.

## Future Development Opportunities

- Depending on how this is meant to integrate in a production setting in the existing product, there are many ways to
  evolve this.
    - If this is really file based, you could set up a trigger on a file being placed in s3 and trigger a Lambda
      function (examples in AWS but this can be easily translated to other cloud providers) to generate a file and land
      it in the desired location;
    - If this is part of a service, you would probably want to expose a RESTful API, e.g., FastAPI or equivalent to
      receive the input data, do the data processing and LLM calls and process them into a sensible response specified
      in an OpenAPI specification or equivalent;
    - Since this does seem time-sensitive, a batch job approach does not seem like a good fit for this use case;
- I have found that demos tend to be quite useful, so either adding a small StreamLit demo on top of this or simply
  exposing a Swagger interface, could be great for this purpose;
- For LLMs, it is essential to think about what happens when things go wrong, e.g., hitting quotas or if the third party
  LLM provider is down. What is the fallback strategy? Do you retry a few times (and with what retry logic) and then
  pivot to a different LLM? Or do you also maintain a more rudimentary fallback option, just repeating the key parts of
  the consultation data?
- Additionally, different variations of prompts could be tested. But for that there should be a feedback mechanism in
  the product letting the user identify their preference or at the least to regenerate the notes.