<!-- If you are submitting a dataset or a model for the model registry please use the corresponding checklists below otherwise feel free to remove them. -->

<!-- add additional description, question etc. related to the new dataset -->


## Checklist
<!-- Please do not delete this -->

- [ ] Run tests locally to make sure nothing is broken using `make test`. 
- [ ] Run the results files checker `make pre-push`.

### Adding a model checklist
<!-- 
When adding a model to the model registry
see also https://github.com/embeddings-benchmark/mteb/blob/main/docs/reproducible_workflow.md
-->

 - [ ] I have added model implementation to `mteb/models/` [directory](https://github.com/embeddings-benchmark/mteb/tree/main/mteb/models). Instruction to add a model can be found [here](https://github.com/embeddings-benchmark/mteb/blob/main/docs/reproducible_workflow.md)
 - [ ] I have ensured that my model can be loaded using
   - [ ] `mteb.get_model(model_name, revision)` and
   - [ ] `mteb.get_model_meta(model_name, revision)`
 - [ ] I have tested the implementation works on a representative set of tasks.