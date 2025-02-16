/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include "login.h"

bool_t
xdr_userDetails (XDR *xdrs, userDetails *objp)
{
	register int32_t *buf;

	int i;
	 if (!xdr_vector (xdrs, (char *)objp->username, 256,
		sizeof (char), (xdrproc_t) xdr_char))
		 return FALSE;
	 if (!xdr_vector (xdrs, (char *)objp->password, 256,
		sizeof (char), (xdrproc_t) xdr_char))
		 return FALSE;
	return TRUE;
}

bool_t
xdr_userStatus (XDR *xdrs, userStatus *objp)
{
	register int32_t *buf;

	 if (!xdr_long (xdrs, &objp->rescode))
		 return FALSE;
	 if (!xdr_long (xdrs, &objp->usercount))
		 return FALSE;
	return TRUE;
}
