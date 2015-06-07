  (define (helper t mp mv lst_parts)
    (cond ((= t 0) (list lst_parts))
	  ((or (< t 0) (<= mp 0) (<= mv 0) (< (* mp mv) t)) ())
	  (else 
	   (define lst_1 (helper (- t mv) (- mp 1) mv (append lst_parts (list mv))))
	   (define lst_2 (helper t mp (- mv 1) lst_parts))
	   (append lst_1 lst_2))))
  (helper total max-pieces max-value ()))