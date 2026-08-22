# ======================================================================
#      LIVE SCHEDULER: PUSH 3 DISTRIBUTED LOAD BALANCER WEIGHTS
# ======================================================================

def get_best_machine_score(k, qp_proc, qd_proc, rload, freeC):
    # Python code executed safely inside an isolated file string wrapper
    score = (qp_proc[k] * 1100) + (qd_proc[k] * 100) + (rload[k] * 10) + (100 if not freeC[k] else 0)
    return score

print("[SUCCESS] Load balancer score configuration compiled into solution_push3.py!")

def compute_max_batch_size(current_state, base_maxm):
    # Enforcing structural state clamps to prevent T1 and latency overflows
    maxm = base_maxm
    if current_state in ["W_D_POST", "W_P_POST"]:
        maxm = min(maxm, 1536)
    return maxm

print("[SUCCESS] Push 4 stage-specific batch constraints appended to solution_push3.py!")
