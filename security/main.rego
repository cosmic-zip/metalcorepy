package example
default allow_access = false

allow_access if {
	input.age >= 18
}