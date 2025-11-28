import MonteCarlo
import RandomForest
tester=RandomForest.RandomForest("AAPL","2009-01-01")
rets=tester.calculate_returns()
targs=tester.init_target_vector(rets)
feats=tester.init_features(rets)
tester.visualize_data(5,feats,rets,targs)
