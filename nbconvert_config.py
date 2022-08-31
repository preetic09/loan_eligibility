c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['preeti24_final_project.ipynb']
c.NbConvertApp.export_format = 'pdf'
c.Exporter.exclude_output_prompt = True
c.Exporter.exclude_input_prompt = True
c.Exporter.exclude_input = True
c.Exporter.template_file = 'template.tplx'