
def _order_2_linked_disconnected_terms_optimized(A, N, trunc, t_args, dt_args, opt_path_list):
    """Calculate all uniquely linked disconnected terms generated from the wave operator ansatz.
    This means for order 5 we include terms such as (4, 1), (3, 1, 1), (2, 1, 1, 1)
    But not terms (5), (3, 2), (2, 2, 1), (1, 1, 1, 1, 1)
    Uses optimized summation paths generate using `contract_expression` from the `opt_einsum` library.
    """
    # unpack the `t_args` and 'dt_args'
    t_i, *unusedargs = t_args
    dt_i, *unusedargs = dt_args
    # make an iterable out of the `opt_path_list`
    optimized_einsum = iter(opt_path_list)
