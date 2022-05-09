import line_profiler
import perceptrons.multilayer_perceptron as mlp
import ex_2.main as main


profiler = line_profiler.LineProfiler()

#profiler.add_function(selections.roulette)
profiler.add_function(mlp.MultiLayerPerceptron.train)
wrapper = profiler(main.main)
wrapper()


profiler.print_stats(open("line_profiler","w"),output_unit=1)