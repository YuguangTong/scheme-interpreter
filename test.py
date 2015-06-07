from scheme_primitives import *
from scheme_reader import *
from scheme import *
from ucb import main, trace

env = create_global_frame()
eval_func = env.bindings[intern("eval")]
twos = Pair(2, nil)


l1 = read_line("(define (db x) (* 2 x))")
l2 = read_line("(define (sq x) (* x x))")
l3 = read_line("(db 2)")
l4 = read_line("(define (cp f g) (lambda (x) (f (g x))))")
scheme_eval(l1)
scheme_eval(l2)
scheme_eval(l3)
scheme_eval(l4)
