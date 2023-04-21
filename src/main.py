from misc import *
import misc
from utils import *
import sys
from data_class import *
sys.path.append(sys.path[0]+'\\..\\tests\\')
from testEngine import *
from tabulate import tabulate

def main():   
    saved={}
    fails=passing=0
    cli_var=cli(settings(help))
    for k,v in cli_var.items():
        the[k] = v
        saved[k] = v
    
    if the['help'] == True:
        print(help)
    
    else:
        values=[]
        data = DATA(the['file'])
        
        print("Results from Old sway")
        best_old,rest_old,n_evals_old = data.sway_old()
        all_sway_dic = data.stats('mid', data.cols.y, 2)
        values.append(all_sway_dic)
        best_sway_dic = best_old.stats('mid', best_old.cols.y, 2) 
        values.append(best_sway_dic)

        print("Results from Old xpln")
        print(best_old, rest_old)
        rule_old,most_old= data.xpln(best_old,rest_old)
        selects = data.selects(rule_old,data.rows)
        data_selects = [s for s in selects if s!=None]
        data1= data.clone(data_selects)
        xpln1 = data1.stats('mid', data1.cols.y, 2)
        
        # print(rule, most)

        print("Results from New sway")
        best_new,rest_new,n_evals_new = data.sway_new()
        print(best_new, rest_new)
        all_sway_dic = data.stats('mid', data.cols.y, 2)
        best_sway2_dic = best_new.stats('mid', best_new.cols.y, 2) 
        values.append(best_sway2_dic)


        print("Results from New Xpln")     
        rule_new,most_new= data.xpln(best_new,rest_new)
        selects = data.selects(rule_new,data.rows)
        data_selects = [s for s in selects if s!=None]
        data1= data.clone(data_selects)
        xpln2 = data1.stats('mid', data1.cols.y, 2)
        values.append(xpln1)
        values.append(xpln2)
        
        
        table = []
        header = []
        header.append("")
        left_column = ['all', 'sway1', 'sway2','xpln1', 'xpln2']
        k=0
        
        for i in all_sway_dic:
            header.append(i)
        for k1 in left_column:
            val =[]
            val.append(left_column[k])
            
            for j in values[k]:            
                val.append(values[k][j])     
            k+=1
            table.append(val) 
        
        print(tabulate(table, header))

    sys.exit(fails)

if __name__ == "__main__":
    # misc.eg('the', 'show options', the_func)
    # misc.eg('rand', 'demo random number generation', the_rand)
    # misc.eg('some', 'demo of reservoir sampling', some_test)
    # misc.eg('nums', 'demo of NUM', num_test)
    # misc.eg('sym', 'demo SYMS', sym_test)
    # misc.eg('csv', 'reading csv files', csv_test)
    # misc.eg('data', 'showing DATA sets', data_test)
    # misc.eg('clone', 'replicate structure of a DATA', clone_test)
    # misc.eg('cliffs', 'start tests', cliffs_test)
    # misc.eg('dist', 'distance test', dist_test)
    # misc.eg('tree', 'make snd show tree of clusters', tree_test)
    # misc.eg('sway', 'optimizing', sway_test)
    # misc.eg('bins', 'find deltas between best and rest', bins_test)
    misc.eg('xpln', 'explore explanation sets', test_xpln)
    main()