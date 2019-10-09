class Basic():
        
    def __init__(self, max_weight, max_volume, df):
        self.weights = [weight for weight in df['weights']]
        self.volumes = [vol for vol in df['volumes']]
        self.values = [val for val in df['values']]
        self.state_weight = [i for i in range(max_weight+1)]
        self.state_volume = [i for i in range(max_volume+1)]
        
                
    def knap_sack(self, max_weight, max_volume, rounds):
            
        if rounds == 0:
            weight_condition = max_weight >= self.state_weight[max_weight] >= self.weights[rounds]
            volume_condition = max_volume >= self.state_volume[max_volume] >= self.volumes[rounds]
            penalty = -9999.99
                 
            result = max(0, (self.values[rounds] if weight_condition and volume_condition else penalty))

        elif self.state_weight[max_weight] < self.weights[rounds] or \
                self.state_volume[max_volume] < self.volumes[rounds]:

            result = self.knap_sack(self.state_weight[max_weight],self.state_volume[max_volume],rounds-1)

        else:
            tmp3 = self.knap_sack(self.state_weight[max_weight],self.state_volume[max_volume],rounds-1)
            
            tmp4_weight = self.state_weight[max_weight] - self.weights[rounds]
            tmp4_volumes = self.state_volume[max_volume] - self.volumes[rounds]
            tmp4 = self.values[rounds] + self.knap_sack(tmp4_weight,tmp4_volumes,rounds-1)
            
            #print((rounds,[max_weight,max_volume,self.values[rounds],self.weights[rounds],self.volumes[rounds]]))

            result = max(tmp3, tmp4)

        return result


class Knapsack():
    
    data_info = []
    
    def __init__(self, max_cost, max_qb, max_rb, max_wr, max_te, max_d, df):
        self.cost = [c for c in df['Salary']]
        self.qb = [q for q in df['QB']]
        self.rb = [r for r in df['RB']]
        self.wr = [w for w in df['WR']]
        self.te = [t for t in df['TE']]
        self.d = [d for d in df['D']]
        
        self.values = [val for val in df['FPPG']]
        self.state_cost = [i for i in range(max_cost+1)]
        self.state_qb = [i for i in range(max_qb+1)]
        self.state_rb = [i for i in range(max_rb+1)]
        self.state_wr = [i for i in range(max_wr+1)]
        self.state_te = [i for i in range(max_te+1)]
        self.state_d = [i for i in range(max_d+1)]
                
                
    def knap_sack(self, max_cost, max_qb, max_rb, max_wr, max_te, max_d, rounds):
            
        if rounds == 0:
            cost_condition = max_cost >= self.state_cost[max_cost] >= self.cost[rounds]
            qb_condition = max_qb >= self.state_qb[max_qb] >= self.qb[rounds]
            rb_condition = max_rb >= self.state_rb[max_rb] >= self.rb[rounds]
            wr_condition = max_wr >= self.state_wr[max_wr] >= self.wr[rounds]
            te_condition = max_te >= self.state_wr[max_te] >= self.te[rounds]
            d_condition = max_d >= self.state_wr[max_d] >= self.d[rounds]
            penalty = -9999.99
                 
            result = max(0, (self.values[rounds] if cost_condition and qb_condition and rb_condition and wr_condition and te_condition and d_condition else penalty))

        elif self.state_cost[max_cost] < self.cost[rounds] or \
             self.state_qb[max_qb] < self.qb[rounds] or \
             self.state_rb[max_rb] < self.rb[rounds] or \
             self.state_wr[max_wr] < self.wr[rounds] or \
             self.state_te[max_te] < self.te[rounds] or \
             self.state_d[max_d] < self.d[rounds]:
                
                result = self.knap_sack(self.state_cost[max_cost],
                                    self.state_qb[max_qb],
                                    self.state_rb[max_rb],
                                    self.state_wr[max_wr],
                                    self.state_te[max_te],
                                    self.state_d[max_d],
                                    rounds-1)

        else:
            tmp3 = self.knap_sack(self.state_cost[max_cost],
                                  self.state_qb[max_qb],
                                  self.state_rb[max_rb],
                                  self.state_wr[max_wr],
                                  self.state_te[max_te],
                                  self.state_d[max_d],
                                  rounds-1)
            
            tmp4_cost = self.state_cost[max_cost] - self.cost[rounds]
            tmp4_qb = self.state_qb[max_qb] - self.qb[rounds]
            tmp4_rb = self.state_rb[max_rb] - self.rb[rounds]
            tmp4_wr = self.state_wr[max_wr] - self.wr[rounds]
            tmp4_te = self.state_te[max_te] - self.te[rounds]
            tmp4_d = self.state_d[max_d] - self.d[rounds]
            
            tmp4 = self.values[rounds] + self.knap_sack(tmp4_cost,
                                                        tmp4_qb,
                                                        tmp4_rb,
                                                        tmp4_wr,
                                                        tmp4_te,
                                                        tmp4_d,
                                                        rounds-1)

            
            result = max(tmp3, tmp4)

        return result























    