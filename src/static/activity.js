var toplevel = {};


// Page load functionality
function place_question_input(question_str, inputId) {
    $("body").append(`<p>${question_str}  <input class="mathQ" type="text" id=${inputId}></input>`);
}

function place_all_questions(question_data, textStatus, jqXHR) {
    toplevel.question_data = question_data
    for (key in question_data) {
        place_question_input(question_data[key]["question_str"], key)
    }
    // place a submit button
    $("body").append('<p><input type="submit" onclick="submit_results()"></input>');
}

function get_game_type() {
    return $("meta").attr("content");
}

function get_game_data(game_type) {
    jQuery.get(`/gamedata/${game_type.toLowerCase()}`, "", place_all_questions, "json");
}

// Submission functionality
function render_solution_review(q_input_field, solution_test) {
    if (solution_test) {
        q_input_field.parentElement.append("   CORRECT!!!")
    } else {
        q_input_field.parentElement.append("   NO!!!!!!!!!!!!!")
    }
}

function assemble_solution_data(q_input_field) {
    var initialdata = toplevel.question_data[q_input_field.id];
    var solution_data = Object.assign({}, initialdata);
    solution_data.answer = parseInt(q_input_field.value);
    solution_data.is_correct = solution_data.answer === parseInt(initialdata.c);
    solution_data.question_id = q_input_field.id;
    return solution_data;
}

function retrieve_results() {
    return $.map($("input.mathQ"), function (inputitem) {
        solution_data = assemble_solution_data(inputitem);
        render_solution_review(inputitem, solution_data.is_correct);
        return solution_data;
    });
}

function submit_results() {
    var results = retrieve_results();
    console.log(results);
    var game_type = get_game_type();

    // submit post request
    $.ajax({
      url: `/gameresults/${game_type.toLowerCase()}`,
      type: "POST",
      data: JSON.stringify(results),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(){
        return "";
      }
    });
}

$(function () {
    // create the game
    get_game_data(get_game_type());
});
