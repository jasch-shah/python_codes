import numpy as np
import scipy as sp

import logging

log = logging.getLogger('colour_transfer')

eps = np.finfo(float).eps

def colour_transfer_mkl(x0, x1):
	a = np.cov(x0.T)
	b = np.cov(x1.T)

	Da2, Ua = np.linalg.eig(a)
	Da = np.diag(np.sqrt(Da2.clip(eps, None)))

	C = np.dot(np.dot(np.dot(np.dot(Da, Ua.T), b), Ua), Da)

	Dc2, Uc = np.linalg.eig(C)
	Dc = np.diag(np.sqrt(Dc2.clip(eps, None)))

	Da_inv = np.diag(1./(np.diag(Da)))

	t = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(Ua, Da_inv), Uc), Dc), Uc.T), Da_inv.T), Ua.T)

	mx0 = np.mean(x0, axis=0)
	mx1 = np.mean(x1, axis=0)

	return np.dot(x0-mx0, t) + mx1


def 	