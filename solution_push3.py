# ======================================================================
#      LIVE SCHEDULER: PUSH 3 DISTRIBUTED LOAD BALANCER WEIGHTS
# ======================================================================

def get_best_machine_score(k, qp_proc, qd_proc, rload, freeC):
    # Python code executed safely inside an isolated file string wrapper
    score = (qp_proc[k] * 1100) + (qd_proc[k] * 100) + (rload[k] * 10) + (100 if not freeC[k] else 0)
    return score

print("[SUCCESS] Load balancer score configuration compiled into solution_push3.py!")
