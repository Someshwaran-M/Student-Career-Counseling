import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

COURSE = ['EEE','E&I','CSE','IT','Mech']
MARK = 'MARK'
PERFORMANCE = 'Performance'
EXAM = 'EXAM'
GRADE = 'GRADE'
POOR = 'Need to Improve Your Skill in all Subjects'
AVERAGE = 'Concentrate On Maths Subject.'
GOOD = 'Improve Gk Knowledge.'
V_GOOD = 'Improve English Knwoledge'
EXCELLENT = 'Excellent Performance'
low_parameter = [0,0,40,50]
average_parameter = [30,40,50,60]
good_parameter = [40,50,60,70]
v_good_parameter = [50,60,70,80]
excellent_parameter = [65,80,100,100]


def compute_fuzzy(mark, exam, grade):
	
	grade = ctrl.Antecedent(np.arange(0,105,5), EXAM)
	MARK = ctrl.Antecedent(np.arange(0,105,5), MARK)
	marks = ctrl.Antecedent(np.arange(0,105,5), GRADE)
	performance = ctrl.Consequent(np.arange(0,105,5), PERFORMANCE)

	grade[POOR] = fuzz.trapmf(grade.universe, low_parameter)
	grade[AVERAGE] = fuzz.trapmf(grade.universe, average_parameter)
	grade[GOOD] = fuzz.trapmf(grade.universe, good_parameter)
	grade[V_GOOD] = fuzz.trapmf(grade.universe, v_good_parameter)
	grade[EXCELLENT] = fuzz.trapmf(grade.universe, excellent_parameter)

	MARK[POOR] = fuzz.trapmf(MARK.universe, [0,0,45,55])
	MARK[AVERAGE] = fuzz.trapmf(MARK.universe, [35,45,55,65])
	MARK[GOOD] = fuzz.trapmf(MARK.universe, [45,55,65,75])
	MARK[V_GOOD] = fuzz.trapmf(MARK.universe, [55,65,75,85])
	MARK[EXCELLENT] = fuzz.trapmf(MARK.universe, [65,75,100,100])

	marks[POOR] = fuzz.trapmf(marks.universe, low_parameter)
	marks[AVERAGE] = fuzz.trapmf(marks.universe, average_parameter)
	marks[GOOD] = fuzz.trapmf(marks.universe, good_parameter)
	marks[V_GOOD] = fuzz.trapmf(marks.universe, v_good_parameter)
	marks[EXCELLENT] = fuzz.trapmf(marks.universe, excellent_parameter)

	performance[POOR] = fuzz.trapmf(performance.universe, low_parameter)
	performance[AVERAGE] = fuzz.trapmf(performance.universe, average_parameter)
	performance[GOOD] = fuzz.trapmf(performance.universe, good_parameter)
	performance[V_GOOD] = fuzz.trapmf(performance.universe, v_good_parameter)
	performance[EXCELLENT] = fuzz.trapmf(performance.universe, excellent_parameter)


	rule1 = ctrl.Rule(MARK[POOR] & marks[POOR] & grade[POOR], performance[POOR])
	rule2 = ctrl.Rule(MARK[POOR] & marks[AVERAGE] & grade[POOR], performance[POOR])
	rule3 = ctrl.Rule(MARK[POOR] & marks[GOOD] & grade[POOR], performance[AVERAGE])
	rule4 = ctrl.Rule(MARK[POOR] & marks[V_GOOD] & grade[POOR], performance[AVERAGE])
	rule5 = ctrl.Rule(MARK[POOR] & marks[GOOD] & grade[V_GOOD], performance[GOOD])
	rule6 = ctrl.Rule(MARK[POOR] & marks[POOR] & grade[AVERAGE], performance[POOR])
	rule7 = ctrl.Rule(MARK[POOR] & marks[AVERAGE] & grade[AVERAGE], performance[AVERAGE])
	rule8 = ctrl.Rule(MARK[POOR] & marks[GOOD] & grade[AVERAGE], performance[AVERAGE])
	rule9 = ctrl.Rule((MARK[POOR] & marks[GOOD] & grade[GOOD]), performance[GOOD])
	rule10 = ctrl.Rule(MARK[POOR] & marks[EXCELLENT] & grade[GOOD], performance[V_GOOD])
	rule11 = ctrl.Rule(MARK[AVERAGE] & marks[AVERAGE] & grade[GOOD], performance[AVERAGE])
	rule12 = ctrl.Rule(MARK[AVERAGE] & marks[GOOD] & grade[GOOD], performance[GOOD])
	rule13 = ctrl.Rule(MARK[AVERAGE] & marks[V_GOOD] & grade[GOOD], performance[GOOD])
	rule14 = ctrl.Rule(MARK[AVERAGE] & marks[V_GOOD] & grade[V_GOOD], performance[V_GOOD])
	rule15 = ctrl.Rule(MARK[AVERAGE] & marks[AVERAGE] & grade[EXCELLENT], performance[GOOD])
	rule16 = ctrl.Rule(MARK[AVERAGE] & marks[AVERAGE] & grade[AVERAGE], performance[AVERAGE])
	rule17 = ctrl.Rule(MARK[AVERAGE] & marks[POOR] & grade[POOR], performance[POOR])
	rule18 = ctrl.Rule(MARK[AVERAGE] & marks[POOR] & grade[GOOD], performance[AVERAGE])
	rule19 = ctrl.Rule(MARK[GOOD] & marks[AVERAGE] & grade[AVERAGE], performance[AVERAGE])
	rule20 = ctrl.Rule(MARK[GOOD] & marks[EXCELLENT] & grade[EXCELLENT], performance[V_GOOD])
	rule21 = ctrl.Rule(MARK[GOOD] & marks[GOOD] & grade[AVERAGE], performance[GOOD])
	rule22 = ctrl.Rule(MARK[GOOD] & marks[POOR] & grade[POOR], performance[POOR])
	rule23 = ctrl.Rule(MARK[V_GOOD] & marks[EXCELLENT] & grade[V_GOOD], performance[V_GOOD])
	rule24 = ctrl.Rule(MARK[V_GOOD] & marks[V_GOOD] & grade[V_GOOD], performance[V_GOOD])
	rule25 = ctrl.Rule(MARK[V_GOOD] & marks[POOR] & grade[POOR], performance[POOR])
	rule26 = ctrl.Rule(MARK[V_GOOD] & marks[GOOD] & grade[V_GOOD], performance[V_GOOD])
	rule27 = ctrl.Rule(MARK[V_GOOD] & marks[EXCELLENT] & grade[EXCELLENT], performance[EXCELLENT])
	rule28 = ctrl.Rule(MARK[EXCELLENT] & marks[EXCELLENT] & grade[V_GOOD], performance[V_GOOD])
	rule29 = ctrl.Rule(MARK[EXCELLENT] & marks[AVERAGE] & grade[AVERAGE], performance[V_GOOD])
	rule30 = ctrl.Rule(MARK[EXCELLENT] & marks[AVERAGE] & grade[V_GOOD], performance[GOOD])
	rule31 = ctrl.Rule(MARK[EXCELLENT] & marks[AVERAGE] & grade[GOOD], performance[GOOD])
	rule32 = ctrl.Rule(MARK[EXCELLENT] & marks[POOR] & grade[POOR], performance[POOR])
	rule33 = ctrl.Rule(MARK[EXCELLENT] & marks[AVERAGE] & grade[POOR], performance[AVERAGE])
	rule34 = ctrl.Rule(MARK[EXCELLENT] & marks[POOR] & grade[AVERAGE], performance[POOR])
	rule35 = ctrl.Rule(MARK[EXCELLENT] & marks[GOOD] & grade[POOR], performance[GOOD])
	rule36 = ctrl.Rule(MARK[EXCELLENT] & marks[POOR] & grade[GOOD], performance[AVERAGE])
	rule37 = ctrl.Rule(MARK[EXCELLENT] & marks[V_GOOD] & grade[POOR], performance[V_GOOD])
	rule38 = ctrl.Rule(MARK[EXCELLENT] & marks[POOR] & grade[V_GOOD], performance[AVERAGE])
	rule39 = ctrl.Rule(MARK[EXCELLENT] & marks[POOR] & grade[EXCELLENT], performance[GOOD])
	rule40 = ctrl.Rule(MARK[EXCELLENT] & marks[AVERAGE] & grade[EXCELLENT], performance[V_GOOD])
	rule41 = ctrl.Rule(MARK[EXCELLENT] & marks[GOOD] & grade[EXCELLENT], performance[V_GOOD])
	rule42 = ctrl.Rule(MARK[EXCELLENT] & marks[V_GOOD] & grade[EXCELLENT], performance[V_GOOD])
	rule43 = ctrl.Rule(MARK[EXCELLENT] & marks[EXCELLENT] & grade[EXCELLENT], performance[EXCELLENT])


	#grade.view()
	#MARK.view()
	#marks.view()
	#performance.view()

	rule_list = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43]

	performance_ctrl = ctrl.ControlSystem(rule_list)
	perf_analysis = ctrl.ControlSystemSimulation(performance_ctrl)

	perf_analysis.input[MARK] = mark
	perf_analysis.input[GRADE] = grade
	perf_analysis.input[EXAM] = exam

	perf_analysis.compute()

	return (str(perf_analysis.output[PERFORMANCE]))
	#return performance.view(sim=perf_analysis)
	