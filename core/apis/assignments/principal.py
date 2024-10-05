from flask import Blueprint, request, jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, AssignmentStateEnum
from core.models.teachers import Teacher
from core.libs.assertions import assert_found
from .schema import AssignmentSchema, AssignmentGradeSchema
from core.apis.teachers.schema import TeacherSchema


principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    assignments = Assignment.get_all_assignments()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload) :
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    assignment = Assignment.get_by_id(grade_assignment_payload.id)

    if assignment.state == AssignmentStateEnum.DRAFT:
        return APIResponse.error(400)

    assert_found(assignment, 'Assignment not found')

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)

    # return jsonify({"assignment_id": assignment_id, "grade": grade}) 