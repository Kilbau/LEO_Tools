//common arguments
//current point
//current position
//current direction
//lineprim

//move position along direction and create geo
//F move one and create geo
//H move half and create geo
function void lsysMoveGeo(vector c_pos, c_dir; float stepsize; int lineprim)
{
	c_pos  += c_dir * stepsize;
	int c_point = addpoint(0, c_pos);
	addvertex(0, lineprim, c_point);
}

//move position along direction
//f move one
//h move half
function void lsysMove(vector c_pos, c_dir; float stepsize; int lineprim)
{
	c_pos  += c_dir * stepsize;
	int c_point = addpoint(0,c_pos);
	lineprim = addprim(0,"polyline");
	addvertex(0,lineprim,c_point);

}

//rotate and return new c_dir
// + turn right 
// - turn left
function void lsysTurn(vector c_dir, up; float angle)
{
	float radians = radians(angle);
	vector4 quat = quaternion(radians,up);
	c_dir = qrotate(quat,c_dir);
}

// " multiply stepsize
// ! multiply pscale
// ; multiply angle
function void lsysMultValue(float value, multiplier)
{
	value *= multiplier;
}

/*
// _ multiply stepsize
// ? multiply pscale
// @ multiply angle
function float lsysDivValue(float origvalue, divider)
{
	float newvalue = origvalue / divider;
	return newvalue;
}
*/


// ^ pitch up 
// & pitch down 

// T gravity

// J K M copy geo

// \\ roll clockwise
// / roll counter clockwise

// | turn 180 degrees
// * roll 180 degrees

// ~ random value 
// between 0 and default 180

//////////////////////////////////////////////////////////////////////////////
//following is probably used in the recursive string generation and not in the interpretion

// [] create branch 
// % cut of / end branch
// : conditions
// ! negate rule
// : int 

////////////////////////////////////////////////////////////////////////////////
//parameters
// g age of current rule (?)

// i offset into the current string (?)

// t iteration count

////////////////////////////////////////////////////////////////////////////////
//stuff to add
//limit inside shape

