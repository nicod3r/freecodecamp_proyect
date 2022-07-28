import re
'''list_up #escribe la lista superior
list_down #escribe la lista de abajo
signal_up #escribir el sigo de arriba de la cuenta final
signal_down #escribrir el sigo en la cuenta final
int_list_up # lista superior para sumar
int_list_down #lista inferior para sumar
result #escribe la lista del resultado final'''
#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
def arithmetic_arranger(list, resolution):
    list 
    resolution 
    ######################################################################################################
    list_up = []
    list_down = []
    c = len(list) # c permite contar la cantidad de veces que se necesita iterar la lista.
    i = 0
    signal_up = []
    signal_down = []
    int_list_up = []
    int_list_down = []
    if len(list) < 6:
        while i < c:
            x = re.findall('[0-9]+',list[i])
            #print(list[i])
            digit = re.findall('[a-z]',list[i])
            if len(digit) == 0:
                digit = 0
                #print ('0k') 
            else:
                print("Error: Numbers must only contain digits.")
                break
            signal = re.findall('[-+]',list[i])
            if signal == ['+']:
                signal_down.append('+')
            elif signal == ['-']:
                signal_down.append('-')
            else:
                print("Error: Operator must be '+' or '-'.")
                break
            #print(signal_down)
            i = i + 1
            list_up.append(x[0])
            if len(x[0]) > 4:
                print('Error: Numbers cannot be more than four digits.')
                break
            list_down.append(x[1])
            if len(x[1]) > 4:
                print('Error: Numbers cannot be more than four digits.')
                break
        #print('lista superior',list_up)
        #print('lista inferior',list_down)
        for x in list_up:
            int_x = int(x)
            int_list_up.append(int_x)
        for y in list_down:
            int_y = int(y)
            int_list_down.append(int_y)
        #print('lista superior de enteros',int_list_up)
        #print('lista inferior de enteros',int_list_down)
        resolve = True
        if resolve == True:
            result = []
            v = 0
            result_final = []
            while v < c:
                if signal_down[v] == '+':
                    result.append(int_list_up[v] + int_list_down[v])
                else:
                    result.append(int_list_up[v] - int_list_down[v])
                #print(result)
                v = v + 1
        else:
            result = []
        #####################################################################################################
        # Escribir los numeros de forma ordenada.
        j = 0
        l_list_up = []
        l_list_down = []
        l_bar = []
        l_result = []
        while j < c:
            der = list_up[j]
            #print(der)
            der_s = list_down[j]
            #print(der)
            re_s = str(result[j])
            der_counts = len(der)
            der_counts_s = len(der_s)
            re_counts = len(re_s)
            if len(der)>len(der_s):
                total_space = len(der)
                #print(total_space)
            else:
                total_space = len(der_s)
            x = total_space - len(der)
            l_list_up.append('  '+ x*' ' + der)
            y = total_space - len(der_s)
            l_list_down.append(signal_down[j] + ' '+ (y)*' ' + der_s)
            l_bar.append(total_space*'-'+ '--')
            k = len(total_space*'-'+ '--') - len(re_s)
            l_result.append((k)*' ' + re_s)
            j = j + 1
        #print(l_list_up)
        #print(l_list_down)
        #print(l_bar)
        #print(l_result)
        p = ''
        g = 0
        for t in l_list_up:
            p = p + t
            if g >= 0 and g < len(list):
                p = p + '    '
            g = g + 1

        print (p)
        q = ''
        l = 0
        for a in l_list_down:
            q = q + a
            if l >= 0 and l < len(list):
                q = q + '    '
            l= l + 1
        print (q)
        o = ''
        m = 0
        for w in l_bar:
            o = o + w
            if m >= 0 and m < len(list):
                o = o + '    '
            m= m + 1
        print (o)
        ######################################
        if resolution == True:       
            qr = ''
            lr = 0
            for ar in l_result:
                qr = qr + ar
                if lr >= 0 and lr < len(list):
                    qr = qr + '    '
                lr= lr + 1
            print (qr)
        else:
            None
    else:
        print('Error: Too many problems.')
arithmetic_arranger(['1+1','30+10','40+500','10-532','52-10'],False)