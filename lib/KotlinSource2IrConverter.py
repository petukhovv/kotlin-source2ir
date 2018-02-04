import os

from .helpers.TimeLogger import TimeLogger
from .helpers.FilesWalker import FilesWalker
from .helpers.IrText2JsonConverter import IrText2JsonConverter


class KotlinSource2IrConverter:
    @staticmethod
    def convert(compiler_path, input_folder, output_folder):
        files_info = {
            'all': 0,
            'current': 0
        }

        def files_count(filename):
            files_info['all'] += 1

        def file_process(filename):
            files_info['current'] += 1

            time_logger = TimeLogger(task_name='Parsing to IR %d of %d (%s)'
                                               % (files_info['current'], files_info['all'], filename))
            # subprocess.call([compiler_path, filename])

            relative_filename = os.path.relpath(filename, input_folder)
            output_file = output_folder + '/' + relative_filename
            file_folder = os.path.dirname(output_folder + '/' + relative_filename)
            if not os.path.exists(file_folder):
                os.makedirs(file_folder)

            ir = IrText2JsonConverter(filename).convert()

            with open('%s.json' % output_file, 'w') as f:
                f.write(ir)

            time_logger.finish()

        # Count source code files stage
        FilesWalker.walk(input_folder, files_count, extension='txt')

        # Parsing source code files stage
        FilesWalker.walk(input_folder, file_process, extension='txt')

